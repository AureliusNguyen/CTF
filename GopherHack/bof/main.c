#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
	int key;
	char overflowme[32];

	setbuf(stdin, NULL);


	key = 0xdeadbeef;
	printf("overflow me : ");
	fflush(stdout);
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		system("cat flag.txt");
	}
	else{
		printf("Nah..\n");
	}
	return 0;
}

