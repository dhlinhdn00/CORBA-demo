
# CORBA Demo Project with OmniORB
This project serves as a presentation on Distributed System Architecture, in the subject SOA - semester 9 - class 20PFIEV3 - The University of Danang - University of Science and Technology.
## Overview
This project demonstrates the use of **CORBA (Common Object Request Broker Architecture)** with **OmniORB** for creating client-server applications in both **C++** and **Python**. The project contains two demos:
- **Basic_Demo**: A simple addition task implemented in both C++ and Python, compatible with both Windows and Linux.
- **Advanced_Demo**: A more complex demo where the client requests a text generation task using a large language model (CausalLM), executed on a server equipped with a GPU.

### About OmniORB
**OmniORB** is a robust CORBA implementation supporting **C++** and **Python**. It is available for both **Linux** and **Windows** environments, offering high compatibility across different platforms.

Official documentation: [OmniORB Documentation](https://omniorb.sourceforge.io/docs.html)

## Project Structure

```bash
.
├── Advanced_Demo
│   ├── Advanced_Demo
│   │   └── __init__.py
│   ├── Advanced_Demo__POA
│   │   └── __init__.py
│   ├── Client.py
│   ├── QA.idl
│   ├── QA_idl.py
│   └── Server.py
├── Basic_Demo_C++
│   ├── Basic_Demo.hh
│   ├── Basic_Demo.idl
│   ├── Basic_DemoSK.cc
│   ├── client
│   ├── Client.cpp
│   ├── ior.txt
│   ├── server
│   └── Server.cpp
├── Basic_Demo_Python
│   ├── Basic_Demo
│   │   └── __init__.py
│   ├── Basic_Demo.idl
│   ├── Basic_Demo__POA
│   │   └── __init__.py
│   ├── Basic_Demo_idl.py
│   ├── Client.py
│   ├── ior.txt
│   └── Server.py
└── README.md
```

### Branches
- **default-ver**: Contains the uncompiled source code and IDL files.
- **client-side**: Contains files for running the client-side of the demo.
- **server-side**: Contains files for running the server-side of the demo.
- **main**: Contains all the source code for both client and server.

## Setup Instructions

### C++ Demo

#### Installing OmniORB

- **Linux**: 
  The latest version as of now (September 6, 2024) of **omniORB-4.3.2** can be installed on Linux.
  
- **Windows**: 
  For Windows, only versions **4.2.0** and below are supported.
  
  Download the appropriate version from the official [SourceForge page](https://sourceforge.net/projects/omniorb/files/omniORB/).

#### Compilation on Linux
1. Download and extract OmniORB.
2. Compile using `make`:
   ```bash
   make
   ```

#### Compilation on Windows
1. Use **msys2** to compile. We recommend downgrading **g++** to a version from around 2013 or 2014 to ensure compatibility.
   
   ```bash
   pacman -S mingw-w64-x86_64-toolchain
   ```

2. Compiling the Code. In the msys2 terminal, navigate to the extracted OmniORB directory. Then using `make`:
   ```bash
   cd /path/to/omniorb/directory
   make
   ```

#### Compiling IDL Files

For C++:

```bash
omniidl -bcxx Basic_Demo.idl
```

This will generate `Basic_Demo.hh` and `Basic_DemoSK.cc`.

#### Compiling the C++ Demo

```bash
g++ -o client Client.cpp Basic_DemoSK.cc -I/usr/local/include -L/usr/local/lib -Wl,-rpath,/usr/local/lib -lomniORB4 -lomnithread
g++ -o server Server.cpp Basic_DemoSK.cc -I/usr/local/include -L/usr/local/lib -Wl,-rpath,/usr/local/lib -lomniORB4 -lomnithread
```

### Python Demo

The Python demo is simpler to set up. Install **omniORBpy** via **pip**:

```bash
pip install omniorb-py
```

Compile the IDL file for Python:

```bash
omniidl -bpython Basic_Demo.idl
```

This will generate the necessary files: two folders containing `__init__.py` and `Basic_Demo_idl.py`.

To run the demo:

```bash
python Client.py
python Server.py
```

## Demo Overview

### Basic_Demo
The **Basic_Demo** performs a simple addition of two numbers, `a` and `b`. It is implemented in both Python and C++ and can run across **Linux** and **Windows** platforms. The demo highlights **CORBA's cross-platform compatibility** by allowing any combination of client-server implementations between C++ and Python, on different operating systems.

The client connects to the server using the **IOR** string, which is stored in the `ior.txt` file. We have automated the process to print the IOR for convenience.

### Advanced_Demo
In the **Advanced_Demo**, a more complex task is performed: text generation using a **CausalLM** model (`bigscience/bloom-560m`). This task typically requires a **GPU** for optimal performance. The client machine, which lacks a GPU, can still perform text generation by offloading the task to a server equipped with an **RTX 3060** (4GB VRAM).

This demo showcases **distributed computing**—allowing clients to leverage the hardware resources of the server. You can replace the model with larger, more powerful ones (e.g., **Llama-3**, **Mistral**) if the server's hardware supports it.

Dependencies for the Advanced Demo include:
- **transformers**
- **torch**

Install them with:

```bash
pip install transformers torch
```

## Reference Documentation
For more information and detailed code explanations, refer to the [official OmniORB documentation](https://omniorb.sourceforge.io/docs.html).
