#include <stdio.h>

int main(void) {

  FILE *file;
  const int nx = 10;
  /* In C, float is float32 */
  float float_array[nx];
  /* in C, short int is int16 */
  short int int_array[nx];
  int i;

  for (i = 0; i < nx; i++) {
    float_array[i] = i * 1.5;
    int_array[i] = i * 2;
  }

  file = fopen("data/c-data_float.bin", "wb");
  fwrite(float_array, sizeof(float_array), 1, file);
  fclose(file);

  file = fopen("data/c-data_int.bin", "wb");
  fwrite(int_array, sizeof(int_array), 1, file);
  fclose(file);

  return 0;
}
