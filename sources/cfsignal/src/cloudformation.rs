use crate::error::{self, Result};

use aws_config::BehaviorVersion;
use aws_smithy_experimental::hyper_1_0::{CryptoMode, HyperClientBuilder};
use aws_types::region::Region;
use imdsclient::ImdsClient;
use log::info;
use snafu::{OptionExt, ResultExt};
use std::env;
use std::str::FromStr;

/// Signals Cloudformation stack resource
pub async fn signal_resource(
    stack_name: String,
    logical_resource_id: String,
    status: String,
) -> Result<()> {
    info!("Connecting to IMDS");
    let _ = rustls::crypto::aws_lc_rs::default_provider().install_default();
    let mut client = ImdsClient::new();
    let instance_id = get_instance_id(&mut client).await?;
    let region = get_region(&mut client).await?;

    info!(
        "Region: {:?} - InstanceID: {:?} - Signal: {:?}",
        region, instance_id, status
    );
    let config = aws_config::defaults(BehaviorVersion::v2024_03_28())
        .region(Region::new(region.to_owned()))
        .load()
        .await;

    #[cfg(feature = "fips")]
    let crypto_mode = CryptoMode::AwsLcFips;
    #[cfg(not(feature = "fips"))]
    let crypto_mode = CryptoMode::AwsLc;

    let https_proxy: Option<String> = match env::var_os("HTTPS_PROXY") {
        Some(https_proxy) => https_proxy.to_str().map(|h| h.to_string()),
        _ => None,
    };

    let no_proxy: Option<Vec<String>> = match env::var_os("NO_PROXY") {
        Some(no_proxy) => no_proxy
            .to_str()
            .map(|n| n.split(',').map(|s| s.to_string()).collect()),
        _ => None,
    };

    let http_client = if let Some(https_proxy) = https_proxy {
        let no_proxy = no_proxy.as_deref();
        HyperClientBuilder::new()
            .crypto_mode(crypto_mode)
            .build_with_proxy(https_proxy, no_proxy)
    } else {
        HyperClientBuilder::new()
            .crypto_mode(crypto_mode)
            .build_https()
    };

    let cloudformation_config = aws_sdk_cloudformation::config::Builder::from(&config)
        .http_client(http_client)
        .build();

    let client = aws_sdk_cloudformation::Client::from_conf(cloudformation_config);

    client
        .signal_resource()
        .stack_name(stack_name)
        .logical_resource_id(logical_resource_id)
        .status(
            aws_sdk_cloudformation::types::ResourceSignalStatus::from_str(&status)
                .expect("infallible"),
        )
        .unique_id(instance_id)
        .send()
        .await
        .context(error::SignalResourceSnafu)?;

    Ok(())
}

/// Returns the instanceId
async fn get_instance_id(client: &mut ImdsClient) -> Result<String> {
    client
        .fetch_instance_id()
        .await
        .context(error::ImdsRequestSnafu)?
        .context(error::ImdsNoneSnafu {
            what: "instance-id",
        })
}

/// Returns the region
async fn get_region(client: &mut ImdsClient) -> Result<String> {
    client
        .fetch_region()
        .await
        .context(error::ImdsRequestSnafu)?
        .context(error::ImdsNoneSnafu { what: "region" })
}
