#include <stdint.h>
#include <stdio.h>

#include "mxc_device.h"
#include "mxc_delay.h"


int main(void) {
    // configure output
    mxc_gpio_cfg_t gpio_rgb_r_out;
    gpio_rgb_r_out.port = MXC_GPIO2;
    gpio_rgb_r_out.mask = MXC_GPIO_PIN_0;
    gpio_rgb_r_out.pad = MXC_GPIO_PAD_NONE;
    gpio_rgb_r_out.func = MXC_GPIO_FUNC_OUT;

    while (1) {
        MXC_GPIO_OutSet(gpio_rgb_r_out.port, gpio_rgb_r_out.mask);
        MXC_Delay(250000);
        MXC_GPIO_OutClr(gpio_rgb_r_out.port, gpio_rgb_r_out.mask);
        MXC_Delay(250000);
    }
}