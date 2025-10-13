# [Wide3 radio telescope](https://www.wide3.com)

## [viewer](./viewer)

contains an implementation of the [RsInstrument](https://pypi.org/project/RsInstrument/) library for controlling Rhode&Schwarz devices. It has been tested intensively on the [FPC1500](https://www.rohde-schwarz.com/products/test-and-measurement/benchtop-analyzers/rs-fpc-spectrum-analyzer_63493-542324.html) R&S Spectrum analyzer

## [waterfall](/.waterfall)

contains an implementation of the waterfall visualization with the time-intensity and frequency-intensity projection

## [control](./control)

the control software divided in [keypad](./control/keypad/) and [server](./control/server/)

### [keypad](./control/keypad/)

the partable implementation of a keyboard to control the mount

### [server](./control/server/)

the server to install on the server control board (every device is a server)

## [tests](./tests)

Contains anything not yet ready for general use. It contains tests on the control hardware device drivers, reception tests, the receiver implementation, and configuration scripts that have not yet been fully developed.
