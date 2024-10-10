import time
import numpy as np
from RsInstrument import *
from datetime import datetime


def time_slice(spectrum_values, cent=None, span=None, start=None, stop=None):
    freq_start = None
    freq_stop = None
    if cent and span:
        freq_start = cent-span
        freq_stop = cent+span
    elif cent and start:
        freq_start = start
        freq_stop = 2 * start - cent
    elif cent and stop:
        freq_start = 2 * cent - stop
        freq_stop = stop
    elif span and start:
        freq_start = start
        freq_stop = start + 2 * span
    elif span and stop:
        freq_start = stop - 2 * span
        freq_stop = stop
    elif start and stop:
        freq_start = start
        freq_stop = stop

    frequencies = np.linspace(freq_start, freq_stop, len(spectrum_values))
    return dict(zip(frequencies, spectrum_values))
    
instr_list = RsInstrument.list_resources("?*")
if instr_list:
    instr_conn = instr_list[0]
    instr = RsInstrument(instr_conn, id_query=True, reset=True)
    idn = instr.query_str('*IDN?')
    print(f"\nHello, I am: '{idn}'")
    print(f'RsInstrument driver version: {instr.driver_version}')
    print(f'Visa manufacturer: {instr.visa_manufacturer}')
    print(f'Instrument full name: {instr.full_instrument_model_name}')
    print(f'Instrument installed options: {",".join(instr.instrument_options)}')
    
    instr.write("SYST:BEEP:KEY:VOL 0")
    instr.write("SYST:BEEP:POV ON")
    instr.write("SYST:BEEP:VOL 1")
    instr.write("SYST:DISP:UPD ON")

    current_dateTime = datetime.now()
    instr.write(f"SYST:DATE {current_dateTime.year},{current_dateTime.month},{current_dateTime.day}")
    instr.write(f"SYST:TIME {current_dateTime.hour},{current_dateTime.minute},{current_dateTime.second}")
    instr.write("SYST:TZON 01,00")
    instr.write("UNIT:LENG MET")
    
    instr.write('INST:SEL SAN')
    central_frequency = 2.45e9  # Hz
    instr.write(f'SENS:FREQ:CENT {central_frequency}')
    
    span_value = 20e6  # 20 MHz in Hz
    instr.write(f'SENS:FREQ:SPAN {span_value}')
    
    sweep_time = 50e-3  # 50 milliseconds in seconds
    instr.write(f'SENS:SWE:TIME {sweep_time}')

    # instr.write('SENS:BAND:RES 1000KHZ')  # Resolution bandwidth
    # instr.write('SENS:BAND:RES 1000KHZ')  # Video bandwidth

    instr.write('UNIT:POW W')
    instr.write('INIT:CONT OFF')
    time.sleep(1)

    spectrogram = {}
    for i in range(10):
        instr.write('INIT:IMM')
        instr.query_opc()
        
        spectrum_data = instr.query_str('TRACE:DATA?')
        spectrum_values = [float(value) for value in spectrum_data.split(',')]
        slice = time_slice(spectrum_values, cent=central_frequency, span=span_value)
        spectrogram[datetime.now()] = slice
        
        print(f"{i} acquired spectrum data. Total power (W): {sum(spectrum_values)}")

        time.sleep(0.1)

    print(spectrogram)
