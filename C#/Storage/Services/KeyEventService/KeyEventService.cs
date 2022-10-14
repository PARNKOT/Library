using System.Threading;

namespace Storage.Services.KeyEventService
{
    public class KeyEventService : IKeyEventsService
    {
        public async void Stub()
        {
            Console.WriteLine("KeyEventService Stub() works!");
            //new Thread(listen).Start();
            //thread.Start();

            await listen();
        }

        public async Task listen()
        {
            while (true) {
                Console.WriteLine("KeyEventService is working...");
                Thread.Sleep(5000);
            }
        }

        public Task StartAsync()
        {
            Console.WriteLine("KeyEventService StartAsync() works!");
            return Task.CompletedTask;
        }
    }
}
