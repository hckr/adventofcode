using System;
using System.Collections.Generic;
using System.Linq;

namespace _1
{
    class Program
    {
        static void Main(string[] args)
        {
            var changes = new List<int>();
            string line;
            while(!string.IsNullOrEmpty(line = Console.ReadLine()))
            {
                changes.Add(int.Parse(line));
            }

            // part one
            Console.WriteLine(changes.Sum());

            // part two
            int frequency = 0;
            var previousFrequencies = new HashSet<int>();
            previousFrequencies.Add(frequency);

            while (true)
            {
                foreach (var change in changes)
                {
                    frequency += change;
                    if (previousFrequencies.Contains(frequency))
                    {
                        Console.WriteLine(frequency);
                        System.Environment.Exit(0);
                    }
                    previousFrequencies.Add(frequency);
                }
            }
        }
    }
}
