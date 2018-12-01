#include <iostream>
#include <vector>
#include <iterator>
#include <numeric>
#include <unordered_set>


int main() {
    using number = int;
    auto changes = std::vector<number>();
    std::copy(std::istream_iterator<number>(std::cin), std::istream_iterator<number>(), std::back_inserter(changes));

    // part one
    std::cout << std::accumulate(changes.begin(), changes.end(), 0) << "\n";

    // part two
    number frequency = 0;
    auto previous_frequencies = std::unordered_set{frequency};
    previous_frequencies.insert(frequency);

    while(1) {
        for (const auto& change : changes) {
            frequency += change;
            if (previous_frequencies.count(frequency)) {
                std::cout << frequency << "\n";
                std::exit(0);
            }
            previous_frequencies.insert(frequency);
        }
    }

    return 0;
}
