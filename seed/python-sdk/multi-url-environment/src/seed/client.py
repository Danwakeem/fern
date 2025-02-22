# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import SeedMultiUrlEnvironmentEnvironment
from .resources.ec_2.client import AsyncEc2Client, Ec2Client
from .resources.s_3.client import AsyncS3Client, S3Client


class SeedMultiUrlEnvironment:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - environment: SeedMultiUrlEnvironmentEnvironment. The environment to use for requests from the client. from .environment import SeedMultiUrlEnvironmentEnvironment

                                                           Defaults to SeedMultiUrlEnvironmentEnvironment.PRODUCTION

        - token: typing.Union[str, typing.Callable[[], str]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from seed.client import SeedMultiUrlEnvironment

    client = SeedMultiUrlEnvironment(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        environment: SeedMultiUrlEnvironmentEnvironment = SeedMultiUrlEnvironmentEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            environment=environment,
            token=token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.ec_2 = Ec2Client(client_wrapper=self._client_wrapper)
        self.s_3 = S3Client(client_wrapper=self._client_wrapper)


class AsyncSeedMultiUrlEnvironment:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - environment: SeedMultiUrlEnvironmentEnvironment. The environment to use for requests from the client. from .environment import SeedMultiUrlEnvironmentEnvironment

                                                           Defaults to SeedMultiUrlEnvironmentEnvironment.PRODUCTION

        - token: typing.Union[str, typing.Callable[[], str]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from seed.client import AsyncSeedMultiUrlEnvironment

    client = AsyncSeedMultiUrlEnvironment(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        environment: SeedMultiUrlEnvironmentEnvironment = SeedMultiUrlEnvironmentEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            environment=environment,
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.ec_2 = AsyncEc2Client(client_wrapper=self._client_wrapper)
        self.s_3 = AsyncS3Client(client_wrapper=self._client_wrapper)
