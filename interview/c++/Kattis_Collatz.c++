#include <iostream>
#include <vector>
#include <list>
using namespace std;

void print_results(unsigned long long i, unsigned long long j, unsigned long long i_steps, unsigned long long j_steps, unsigned long long meeting) {
    cout << i << " needs " << i_steps << " steps, " << j;
    cout << " needs " << j_steps << " steps, they meet at ";
    cout << meeting << endl;
}

void compute(unsigned long long num, vector<unsigned long long>& steps) {
    steps.push_back(num);
    while (num != 1) {
        if (num % 2 == 0) {
            num /= 2;
        } else {
            num = (3 * num) + 1;
        }
        steps.push_back(num);
    }
}

int main() {
    unsigned long long i = -1;
    unsigned long long j = -1;
    while (true) {
        cin >> i;
        cin >> j;
        if (i == 0) {
            break;
        }
        vector<unsigned long long> i_steps;
        vector<unsigned long long> j_steps;
        compute(i, i_steps);
        compute(j, j_steps);
        unsigned long long i_req_steps;
        unsigned long long j_req_steps;
        unsigned long long meeting = 0;
        bool found_steps = false;
        for (i_req_steps = 0; i_req_steps < (unsigned long long) i_steps.size() && !found_steps; i_req_steps++) {
            for (j_req_steps = 0; j_req_steps < (unsigned long long) j_steps.size() && !found_steps; j_req_steps++) {
                if (i_steps[i_req_steps] == j_steps[j_req_steps]) {
                    found_steps = true;
                    meeting = i_steps[i_req_steps];
                }
            }
        }
        print_results(i, j, i_req_steps - 1, j_req_steps - 1, meeting);
    }
    return 0;
}
