#include <iostream>
#include <vector>
#include <tuple>

int grid_serial_number;
std::vector<std::vector<int>> power_levels;

int power_level(int x, int y) {
    int rack_id = x + 10;
    return ((rack_id * y + grid_serial_number) * rack_id) / 100 % 10 - 5;
}

auto best_square(int size=3) {
    int highest_power = 0;
    std::pair<int, int> coordinates;
    int max_x = 300 - size;
    int max_y = 300 - size;
    for (int x = 0; x < max_x; ++x) {
        for (int y = 0; y < max_y; ++y) {
            int square_power = 0;
            for (int i = 0; i < size; ++i) {
                for (int j = 0; j < size; ++j) {
                    square_power += power_levels[x+i][y+j];
                }
            }
            if (square_power > highest_power) {
                highest_power = square_power;
                coordinates = { x, y };
            }
        }
    }
    return std::make_pair(coordinates, highest_power);
}

auto best_square_any_size(int min_size, int max_size) {
    int highest_power = 0;
    std::pair<int, int> coordinates;
    int best_size;
    for (int size = min_size; size <= max_size; ++size) {
        std::cerr << "\rTrying sqare size " << size << "...";
        auto [coords, power] = best_square(size);
        if (power > highest_power) {
            highest_power = power;
            coordinates = coords;
            best_size = size;
        }
    }
    std::cerr << "\n";
    return std::make_tuple(coordinates.first, coordinates.second, best_size);
}

int main(int argc, char const *argv[]) {
    std::cin >> grid_serial_number;

    power_levels.reserve(300);
    for (int x = 0; x < 300; ++x) {
        power_levels[x].reserve(300);
        for (int y = 0; y < 300; ++y) {
            power_levels[x][y] = power_level(x, y);
        }
    }

    auto [ x, y, size ] = best_square_any_size(1, 300);
    std::cout << x << "," << y << "," << size << "\n";

    return 0;
}
