
namespace AzureCDNWebApp.Controllers
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using System.IO;
    using Microsoft.WindowsAzure.Storage;
    using Microsoft.WindowsAzure.Storage.Blob;
    using Microsoft.WindowsAzure.Storage.Auth;
    using System.Net.Http;
    using Microsoft.AspNetCore.Http;
    using Microsoft.Extensions.Options;
    using AzureCDNWebApp.Models;
    using AzureCDNWebApp.Helpers;

    public class ImagesController : Controller
    {
        private readonly AzureStorageConfig storageConfig = null;


        public ImagesController(IOptions<AzureStorageConfig> config)
        {
            storageConfig = config.Value;
        }


        public async Task<IActionResult> Index()
        {
            try
            {
                if (storageConfig.AccountKey == string.Empty || storageConfig.AccountName == string.Empty)
                {
                    return BadRequest("sorry, can't retrieve your azure storage details from appsettings.js, make sure that you add azure storage details there");
                }

                if (storageConfig.ImageContainer == string.Empty)
                {
                    return BadRequest("Please provide a name for your image container in the azure blob storage");
                }

                List<string> imageUrls = await StorageHelper.GetImagelUrls(storageConfig);
                var imagesViewModel = new ImagesViewModel();
                imagesViewModel.ImageUrls = imageUrls;
                return View(imagesViewModel);
            }
            catch (Exception exception)
            {
                return View();
            }
        }


    }
}