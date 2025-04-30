using Kernel;
using Kernel.Models;

namespace Client
{
    public class Program
    {
        public static void Main()
        {
            UDoVariables.Get(Environment.CurrentDirectory, "192.168.1.67", true);
            Console.WriteLine($"Domain folder: {UDoVariables.Get().DomainFolder}");
            Console.WriteLine($"Host: {UDoVariables.Get().Host}");
            Console.WriteLine($"Website: {UDoVariables.Get().Website}");
            Console.WriteLine($"Device: {UDoVariables.Get().PersonalData.DeviceID}");
            Console.WriteLine($"IDDeviceType: {UDoVariables.Get().PersonalData.IdDeviceType}");
            Console.WriteLine($"Allow prerelease: {UDoVariables.Get().PersonalData.AllowPrerelease}");

            Console.WriteLine("Subscribing data callback");
            Interaction.Get().UDeviceDataResultCallback = static (UDeviceData? res) => Console.WriteLine($"DateTime: {DateTime.Now}, ID: {res?.Id}, Owner: {res?.Name}");

            Console.WriteLine("Subscribing exception");
            Interaction.Get().ExceptionCallback = static (ref Exception ex, ref Command command) =>
            {
                ConsoleColor color = Console.ForegroundColor;
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"ERROR during the execution of {command.Task} command: {command.Task} {string.Join(',', command.Args)}");
                Console.WriteLine($"{ex.Message}");
                Console.ForegroundColor = color;
            };

            // Move the radiotelescope to a specific position and stay
            Console.WriteLine("Subscribing command [point]");
            Interaction.Get().AddTaskSubscription("point", static (ref Command command) =>
            {
                ConsoleColor color = Console.ForegroundColor;
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"Received {command.Task} command: {command.Task} {string.Join(',', command.Args)}");
                Console.ForegroundColor = color;

                return true;
            });

            // Scan an area
            Console.WriteLine("Subscribing command [scan]");
            Interaction.Get().AddTaskSubscription("scan", static (ref Command command) =>
            {
                ConsoleColor color = Console.ForegroundColor;
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"Received {command.Task} command: {command.Task} {string.Join(',', command.Args)}");
                Console.ForegroundColor = color;

                return true;
            });

            // Track a given position
            Console.WriteLine("Subscribing command [track]");
            Interaction.Get().AddTaskSubscription("track", static (ref Command command) =>
            {
                ConsoleColor color = Console.ForegroundColor;
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"Received {command.Task} command: {command.Task} {string.Join(',', command.Args)}");
                Console.ForegroundColor = color;

                return true;
            });

            // Change polarity
            Console.WriteLine("Subscribing command [polarity]");
            Interaction.Get().AddTaskSubscription("polarity", static (ref Command command) =>
            {
                ConsoleColor color = Console.ForegroundColor;
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"Received {command.Task} command: {command.Task} {string.Join(',', command.Args)}");
                Console.ForegroundColor = color;

                return true;
            });

            // Change band
            Console.WriteLine("Subscribing command [band]");
            Interaction.Get().AddTaskSubscription("band", static (ref Command command) =>
            {
                ConsoleColor color = Console.ForegroundColor;
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"Received {command.Task} command: {command.Task} {string.Join(',', command.Args)}");
                Console.ForegroundColor = color;

                return true;
            });

            Console.WriteLine("Running...");
            SpinWait.SpinUntil(static () => false);
        }
    }
}