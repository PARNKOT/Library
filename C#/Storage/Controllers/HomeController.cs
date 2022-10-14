using Microsoft.AspNetCore.Mvc;

namespace Storage.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
