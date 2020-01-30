using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AzureCDNWebApp.Helpers;
using AzureCDNWebApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;

namespace AzureCDNWebApp.Controllers
{
    public class VideosController : Controller
    {
        private readonly AzureStorageConfig storageConfig = null;


        public VideosController(IOptions<AzureStorageConfig> config)
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

                if (storageConfig.VideoContainer == string.Empty)
                {
                    return BadRequest("Please provide a name for your image container in the azure blob storage");
                }

                List<string> imageUrls = await StorageHelper.GetVideolUrls(storageConfig);
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