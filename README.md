# WoT-microcontroller-servient
> WoT-microcontroller-servient is an implementation of W3C Web of Things Servient for embedded systems. This module allows users to: define W3C WoT Thing Descriptions, generate scripting files (sketches) in Embedded-C programming language executable by microcontrollers to expose Things, compile and flash these sketches.
## How does it work?
This module provides a fully interactive CLI with which users can interact. The CLI has been developed using Python programming language and Click library. Firstly, users can insert all the metadata included in W3C WoT Thing Descriptions and store them in a JSON file. Secondly, after receiving these metadata, the CLI parses and passes them to the Jinja2 template engine. Using this information and others provided by users, the template engine generates a scripting file including the Thing logic. This scripting file is executed by microcontrollers. Finally, using this CLI, it is possibile to compile and flash the scripting file to a specific embedded system. The only supported embedded system is NodeMCU. 
## Prerequisites
This package is only supported by Linux systems.
**Linux**
- Python v3.6.x
- A proper C/C++ compiler toolchain, like GCC
## Usage
### Clone and install
Clone the repository:
`git clone git@github.com:UniBO-PRISMLab/WoT-microcontroller-servient.git`
Go into the repository:
`cd WoT-microcontroller-servient`
Install the package and all dependencies:
`pip install .`
It is **recomended** to install and use the package inside a virtual environment.
### Commands
The application has four commands:
- `start` to begin the wizard to insert Thing Decription metadata
- `build` to insert information for template engine to generate Embedded-C scripting files
- `compile` to compile Embedded-C scripting files
- `flash` to flash Embedded-C scripting files into embedded systems
### Start application
To start the CLI run:
`embeddedWoTServient start`
## License
WoT-microcontroller-servient is released under the MIT License.


