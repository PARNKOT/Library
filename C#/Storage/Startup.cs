using Microsoft.Extensions.FileProviders;

using Storage.Configurations.Database;
using Storage.Services.KeyEventService;


namespace Storage
{
    public class Startup
    {
        public IConfiguration Configuration { get; }

        public Startup(IConfiguration configuration)
        {
            this.Configuration = configuration;
        }

        public void ConfigureServices(IServiceCollection services)
        {
            services.Configure<DatabaseConfiguration>(this.Configuration.GetSection("Database"));
            services.AddSingleton<IKeyEventsService, KeyEventService>();
            services.AddControllersWithViews();
            
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env, IHostApplicationLifetime applicationLifetime)
        {
            applicationLifetime.ApplicationStarted.Register(() => OnStarted(app));

            string frontendPath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "frontend");
            if(Directory.Exists(frontendPath))
            {
                app.UseStaticFiles(new StaticFileOptions
                {
                    FileProvider = new PhysicalFileProvider(frontendPath),
                    RequestPath = new PathString("")
                });
            }

            app.UseRouting();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
            });
        }

        public void OnStarted(IApplicationBuilder app)
        {
            app.ApplicationServices.GetService<IKeyEventsService>()?.Stub();
        }
    }
}
