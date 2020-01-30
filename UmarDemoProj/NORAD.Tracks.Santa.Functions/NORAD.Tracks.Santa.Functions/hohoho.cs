using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace NORAD.Tracks.Santa.Functions
{
    public static class hohoho
    {
        [FunctionName("hohoho")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = null)] HttpRequest req,
            ILogger log)
        {
            return (ActionResult)new OkObjectResult(DateTime.Parse("24-DEC-2018 07:00:00").ToString());
        }
    }
}
