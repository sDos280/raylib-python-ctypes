#include "raudio.c"

// return size of rAudioBuffer
int GetrAudioBufferSize(void)
{
    return sizeof(rAudioBuffer);
}

// return size of rAudioProcessor
int GetrAudioProcessorSize(void)
{
    return sizeof(rAudioProcessor);
}