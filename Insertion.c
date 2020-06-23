#include<stdio.h>
#include<time.h>
#include<unistd.h>
#define MAX 1000
int arr[MAX], key;

void insertionSort(int arr[], int n)
{
   int i, key, j;
   for (i = 1; i < n; i++)
   {
       key = arr[i];
       j = i-1;

       /* Move elements of arr[0..i-1], that are
          greater than key, to one position ahead
          of their current position */
       while (j >= 0 && arr[j] > key)
       {
           arr[j+1] = arr[j];
           j = j-1;
       }
       arr[j+1] = key;
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
    insertionSort(arr, MAX);
    _sleep(1000);//use sleep in exam in code blocks use this as given
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
