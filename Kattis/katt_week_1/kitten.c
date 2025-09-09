#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int main() {
    int kitten;
    scanf("%d", &kitten);

    int parent[MAX];
    for (int i = 0; i < MAX; i++) {
        parent[i] = -2;
    }
    while (1) {
        int p;
        scanf("%d", &p);
        if (p == -1) {
            break;
        }

        int c;
        while (scanf("%d", &c) == 1) {
            parent[c] = p;
            if (getchar() == '\n') {
                break;
            }
        }
    }

    //Climbing from the kitten to the root
    int current = kitten;
    while (current != -1) {
        printf("%d ", current);
        current = parent[current];
    }
    printf("\n");
    return 0;
}