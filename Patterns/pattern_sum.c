# include <stdio.h>

int main() {
    int n,sum = 0;
    // printf("Enter Dimension of nxn matrix: ");
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        perror("Unable to open file");
        return 1;
    }
    fscanf(file, "%d", &n); // Assuming the first number in the file is n
    int a[n+1][n+1]; // Adjusted for 1-based indexing
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            fscanf(file, "%d", &a[i][j]);
        }
    }

    fclose(file);
    // scanf("%d", &n);
    int mid = ((n-1)/2)+1;
    // int a[n][n];
    // for (int i=1; i<=n; i++) {
    //     for (int j=1; j<=n; j++) {
    //         scanf("%d", &a[i][j]);
    //     }
    // }
    printf("\n");

    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            // First pattern Mid columns + 1 && Not mid row and first row and last row
            if (i==1 || i== mid || i==n){
                if (i==1 && j%2!=0){
                    sum += a[i][j];
                    printf("%d\t", a[i][j]);
                }
                else if (i==mid && j%2==0){
                    sum += a[i][j];
                    printf("%d\t", a[i][j]);
                }
                else if (i==n && j>1 && j<n){
                    sum += a[i][j];
                    printf("%d\t", a[i][j]);
                }
                else {
                    printf("C\t");
                }
                
            }
            else{
                if ((j==mid-1) || (j==mid+1)){
                    sum += a[i][j];
                    // printf("i = %d j= %d : %d\n", i, j, a[i][j]);
                    printf("%d\t", a[i][j]);

                }
                else{
                    printf("C\t");
                }
                
            }
        }
        printf("\n");
    }
    
    printf("Total Sum: %d", sum);

    return 0;
}