#include<stdio.h>
#include<time.h>
#include<unistd.h>
#define MAX 1000
int arr[MAX], key;
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    /* create temp arrays */
    int L[n1], R[n2];

    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    /* Copy the remaining elements of L[], if there
       are any */
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there
       are any */
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l+(r-l)/2;

        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);

        merge(arr, l, m, r);
    }
}
int main()
{
    int i,r,result;
    double total_time;
    double start, end;
    //printf("Enter total elements: ");
    //scanf("%d", &num);

    srand(time(NULL));

    //printf("Enter %d elements: ", num);
    for (i = 0; i <= MAX; i++)
    {
        //scanf("%d", &arr[i]);
        arr[i]= i;
     }


    start = clock();
    mergeSort(arr, 0,MAX - 1);
    _sleep(10000);//use sleep in exam in code blocks use this as given
    end = clock();
    //time count stops
    total_time = (((double) (end - start)) / CLOCKS_PER_SEC);
    //calulate total time
    printf("\nTime taken is: %f", total_time);
   /* if(result==1)
        printf("Succesful search\n");
    else
        printf("Unsuccesful search\n"); */

   return 0;
}

