using global::System.Threading.Tasks;
using SeedApi;

namespace Usage;

public class Example0
{
    public async global::System.Threading.Tasks.Task Do() {
        var client = new SeedApiClient(
            clientOptions: new ClientOptions{
                BaseUrl = "https://api.fern.com"
            }
        );

        await client.GetAccountAsync(
            "account_id"
        );
    }

}
