# SQL Expert

## Prerequisites
- Python >= 3.10 and < 3.13
- CUDA Toolkit version 12.x
- Create and activate virtual environment using either from Anaconda/Miniconda or virtualenv
- Dataset used for training is from [here](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql)

## Installing Unsloth on Windows

### 1. Ensure CUDA Toolkit is Installed and Added to the Environment Path

#### Verify Installation:
Run the following command in CMD:
```bash
nvcc --version
```
#### Expected Output (Example):
```bash
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Tue_Feb_27_16:28:36_Pacific_Standard_Time_2024
Cuda compilation tools, release 12.4, V12.4.99
Build cuda_12.4.r12.4/compiler.33961263_0
```

### 2. Ensure MSVC is Installed and Configured

#### Set Environment Variables:
Create `CC`, `CXX`, and `VS_PATH` variables with the path to `cl.exe`, e.g.:
```
C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.43.34808\bin\Hostx64\x64\cl.exe
```

#### Verify Installation:
Run the following command in CMD:
```bash
cl
```
#### Expected Output (Example):
```bash
Microsoft (R) C/C++ Optimizing Compiler Version 19.43.34808 for x64
Copyright (C) Microsoft Corporation.  All rights reserved.

usage: cl [ option... ] filename... [ /link linkoption... ]
```

#### Ensure that when installing using the Visual Studio Installer, below workloads/individual components are installed:
*Workloads:*
- Python development
- Desktop development with C++
- Linux and embedded development with C++

*Individual Components:*
- .NET Framework 4.8 SDK
- .NET Framework 4.7.2 targeting pack
- C# and Visual Basic Roslyn compilers
- MSBuild
- MSVC v143 - VS 2022 C++ x64/x86 build tools
- C++ 2022 Redistributable Update
- C++ CMake tools for Windows
- C++/CLI support for v143 build tools (Latest)
- MSBuild support for LLVM (clang-cl) toolset
- C++ Clang Compiler for Windows (19.1.1)
- Windows 11 SDK (10.0.22621.0)
- Windows Universal CRT SDK
- C++ 2022 Redistributable MSMs

### 3. Download and Install Latest CMake from [here](https://cmake.org/download/)

#### Verify Installation:
Run the following command in CMD:
```bash
cmake --version
```

#### Expected Output (Example):
```bash
cmake version 3.31.4

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

### 4. Install PyTorch 2.6.0 with CUDA Compatibility

#### Install via pip:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

#### Alternative (if downloading is slow):
Download the [wheel file](https://download.pytorch.org/whl/torch/) and install it manually.

### 5. Install Unsloth
```bash
pip install "unsloth[windows] @ git+https://github.com/unslothai/unsloth.git"
```

### 6. Install Triton-Windows

#### Steps:
1. Download the wheel file from [this repository](https://github.com/woct0rdho/triton-windows/releases).
2. Install it via:
```bash
pip install <path_to_downloaded_wheel>
```

### 7. Install xFormers (Based on Your CUDA Version)
```bash
pip3 install -U xformers --index-url https://download.pytorch.org/whl/cu124
```

#### Verify Installation:
```bash
python -m xformers.info
```

#### Expected Output (Example):
```bash
xFormers 0.0.29.post3
pytorch.version: 2.6.0+cu124
pytorch.cuda: available
gpu.name: NVIDIA GeForce RTX 4080 SUPER
is_triton_available: True
...
```

### 8. Install BitsandBytes

#### Steps:
```bash
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git
cd bitsandbytes
cmake -DCOMPUTE_BACKEND=cuda -S .
cmake --build . --config Release
set CUDA_VERSION=124
python setup.py install
```

#### Verify Installation:
```bash
python -m bitsandbytes
```

#### Expected Output (Example):
```bash
CUDA specs: CUDASpecs(highest_compute_capability=(8, 9), cuda_version_string='124', cuda_version_tuple=(12, 4))
PyTorch settings found: CUDA_VERSION=124, Highest Compute Capability: (8, 9).
Checking that the library is importable and CUDA is callable...
SUCCESS!
```

### 9. Install vLLM
```bash
pip install vllm
```

### 10. Install Flash-Attention 2
#### Steps:
1. Download wheel file from [this repository](https://github.com/kingbri1/flash-attention/releases).
2. Install it via:
```bash
pip install <path_to_downloaded_wheel>
```

## Create `.env` File and Define the Following Variables:
```ini
HF_TOKEN_WRITE=your_huggingface_write_token
HF_TOKEN_READ=your_huggingface_read_token
WANDB_API_KEY=your_wandb_api_key
```

- **HF_TOKEN_WRITE** – Create a write-access Hugging Face token [here](https://huggingface.co/settings/tokens).  
- **HF_TOKEN_READ** – Create a read-access Hugging Face token [here](https://huggingface.co/settings/tokens).  
- **WANDB_API_KEY** – Get your API key [here](https://wandb.ai/site).

## Install Requirements
```bash
pip install -r requirements.txt
```