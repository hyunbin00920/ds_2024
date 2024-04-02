#include <stdio.h>
#include <stdlib.h>

struct node {
    int page;
    struct node* next;
};
typedef struct node node_t;

struct LinkedList {
    node_t* head;
    int size;
};
typedef struct LinkedList LL_t;

void initList(LL_t* cache) {
    cache->head = NULL;
    cache->size = 0;
}

void append(LL_t* cache, int page) {
    node_t* newNode = (node_t*)malloc(sizeof(node_t));
    newNode->page = page;
    newNode->next = cache->head;
    cache->head = newNode;
    cache->size++;
}

int findNode(LL_t* cache, int page) {
    node_t* currNode = cache->head;
    while (currNode != NULL) {
        if (currNode->page != page) {
            currNode = currNode->next;
        } else {
            return 1;
        }
    }
    return 0;
}

void remove_page(LL_t* cache, int page) {
    node_t* currNode = cache->head;
    node_t* prevNode = NULL;
    while (currNode->page != page && currNode != NULL) {
        prevNode = currNode;
        currNode = currNode->next;
    }
    if (currNode->page == page) {
        if (prevNode != NULL) {
            prevNode->next = currNode->next;
            append(cache, page);
            cache->size--;
        } else {
            cache->head = currNode->next;
            append(cache, page);
            cache->size--;
        }
    }
}

void pop(LL_t* cache, int index) {
    node_t* currNode = cache->head;

    if (index != 0) {
        node_t* prevNode = NULL;
        for (int i = 0; i < index - 1; i++) {
            prevNode = currNode;
            currNode = currNode->next;
        }
        prevNode->next = currNode->next;
    } else {
        cache->head = currNode->next;
    }
    cache->size--;
}

void do_sim(LL_t* cache, int page, int* cache_hit, int* tot_cnt, int cache_slots) {
    if (*tot_cnt == 0) {
        append(cache, page);
    } else {
        if (findNode(cache, page) != 0) {
            (*cache_hit)++;
            remove_page(cache, page);
        } else {
            if (cache->size + 1 > cache_slots) {
                pop(cache, cache->size);
                append(cache, page);
            } else {
                append(cache, page);
            }
        }
    }
    (*tot_cnt)++;
}

int main() {
    FILE* fp;

    for (int cache_slots = 100; cache_slots < 1001; cache_slots += 100) {
        int page, cache_hit = 0, tot_cnt = 0;
        LL_t* cache = (LL_t*)malloc(sizeof(LL_t));
        initList(cache);

        fp = fopen("./linkbench.trc", "r");
        // fp = fopen("ds_2024/ds_templates/lru_sim/linkbench.trc", "r");

        while (fscanf(fp, "%d", &page) == 1) {
            do_sim(cache, page, &cache_hit, &tot_cnt, cache_slots);
        }
        float hit_ratio = (float)cache_hit / (float)tot_cnt;
        printf("cache_slot = %d, cache_hit = %d, hit_ratio = %.5f\n", cache_slots, cache_hit, hit_ratio);

        fclose(fp);
        free(cache);
    }

    return 0;
}
