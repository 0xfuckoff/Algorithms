#include <stdio.h>
#include <cstdint>

typedef uint32_t u32;

u32 bin_search(u32 a[], u32 f, u32 l, u32 x);

int main(int argc, char *argv[]) {

	u32 my_list[8] = {1, 2, 3, 4, 5, 6, 7, 8};

	printf("%d", bin_search(my_list, 0, sizeof(my_list) / sizeof(my_list[0]), 4));

	return 0;
}

u32 bin_search(u32 a[], u32 f, u32 l, u32 x) {
	if (l >= f) {
		u32 m = f + (l - f) / 2;
		if (a[m] == x) {
			return m;
		} else if (a[m] <= x) {
			return bin_search(a, m + 1, l, x);
		} else {
			return bin_search(a, f, m - 1, x);
		}
	} else {
		return -1;
	}
}
