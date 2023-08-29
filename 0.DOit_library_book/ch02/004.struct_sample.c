# c언어로 만든 데이터 출력
# c언어

// PYStruct.c

#pragma warning(disable:4996)

#include <stdio.h>

typedef struct { // 16바이트  = 13바이트 + 3바이트(null)
	double v;  // 8바이트
	int t;     // 4바이트
	char c;    // 1바이트
} save_type;

typedef struct { // 24바이트  = 18바이트 + 6바이트(null)
	double v;   // 8바이트
	int t;      // 4바이트
	char s[6];    // 6바이트
} save_type2;

int step1();
int step2();

int main() {
	// step1();
	step2();

	return 0;
}

int step1() {
	save_type s = { 7.5f, 15, 'A' };

	int size = sizeof(save_type);
	printf("filename(output2.bin): size(%d)\n", size);

	FILE* f = fopen("output.bin", "w");
	fwrite(&s, size, 1, f);
	fclose(f);

	return 0;
}

int step2() {
	save_type2 s2 = { 7.5f, 15, "Hello" };

	int size2 = sizeof(save_type2);
	printf("filename(output2.bin): size(%d)\n", size2);

	FILE* f = fopen("output2.bin", "w");
	fwrite(&s2, size2, 1, f);
	fclose(f);

	return 0;
}
