using System;
using System.Collections.Generic;
using System.Linq;

namespace _1
{
    class Program
    {
        static void Main(string[] args)
        {
            var masses = new List<int>();

            string line;
            while (!string.IsNullOrEmpty(line = Console.ReadLine()))
            {
                masses.Add(int.Parse(line));
            }

            // part one
            Console.WriteLine(masses.Aggregate(0,
                (fuelRequirements, mass) => fuelRequirements + RequiredFuel(mass)));

            // part two
            Console.WriteLine(masses.Aggregate(0,
                (fuelRequirements, mass) =>
                {
                    var requiredFuel = RequiredFuel(mass);
                    var additionalFuel = RequiredFuel(requiredFuel);
                    while (additionalFuel > 0)
                    {
                        requiredFuel += additionalFuel;
                        additionalFuel = RequiredFuel(additionalFuel);
                    }
                    return fuelRequirements + requiredFuel;
                }));
        }

        static int RequiredFuel(int mass)
        {
            return Math.Max(0, mass / 3 - 2);
        }
    }
}
