#include <stdint.h>
#include <stdio.h>

#include "mxc_device.h"
#include "mxc_delay.h"
#include <mxc.h>

int main(void) {

    uint8_t secs = 0;

    while(1){
        printf("%d\n", secs);
        secs += 1;
        MXC_Delay((uint32_t) 1e6);
    }
}