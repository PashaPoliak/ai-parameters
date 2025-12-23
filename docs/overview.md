# Project Overview: Working with Different LLMs and Parameters

## Introduction

This project provides a comprehensive implementation for working with different Large Language Models (LLMs) and their request parameters via the DIAL API. The primary goal is to understand how various parameters affect LLM output and behavior, enabling developers to fine-tune models for specific use cases.

## Project Goals
- Learn how to work with different LLMs through DIAL API
- Understand how to configure LLM output via request parameters (temperature, n, seed, etc.)
- Implement practical examples for each parameter
- Document the effects and best practices for each parameter

## Architecture Overview

```mermaid
graph TD
    A[Client Application] --> B[DIAL API Client]
    B --> C[Request Parameters]
    C --> D[LLM Models]
    D --> E[Response Processing]
    E --> F[Result Analysis]
    
    C --> C1[Temperature]
    C --> C2[N Completions]
    C --> C3[Seed Value]
    C --> C4[Max Tokens]
    C --> C5[Frequency Penalty]
    C --> C6[Presence Penalty]
    C --> C7[Stop Sequences]
    
    D --> D1[gpt-4o]
    D --> D2[gpt-4.1-nano-2025-04-14]
    D --> D3[gpt-4.1-mini-2025-04-14]
    D --> D4[gemini-2.0-flash-lite]
    D --> D5[gemini-2.0-flash]
    D --> D6[gemini-2.5-pro]
    D --> D7[gemini-2.5-flash]
    D --> D8[claude-3-5-haiku@20241022]
    D --> D9[claude-3-7-sonnet@20250219]
    D --> D10[claude-sonnet-4@20250514]
```

## Core Components

### Models Layer
- `conversation.py` - Handles conversation state and history
- `message.py` - Represents individual messages in a conversation
- `role.py` - Defines roles (system, user, assistant) for messages

### Application Layer
- `main.py` - Entry point and orchestration
- `client.py` - DIAL API communication layer

### Constants and Configuration
- `task/constants.py` - Centralized configuration with API_KEY, DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, and DIAL_ENDPOINT

### Task Implementations
- Series of parameter-specific task files (1_task_models.py through 9-task-additional-parameters.py)

## Implementation Details

### Parameter Implementation Tasks

#### Task 1: Models Exploration
- **File**: `task/1-task-models.py`
- **Functionality**: Implemented model testing functionality to work with different LLMs
- **Features**: Model name validation, response processing, error handling

#### Task 2: N Parameter (Number of Completions)
- **File**: `task/2-task-n.py`
- **Functionality**: Implemented n parameter to generate multiple completions
- **Features**: Multiple choice processing, response aggregation

#### Task 3: Temperature Parameter
- **File**: `task/3-task-temperature.py`
- **Functionality**: Implemented temperature parameter for controlling randomness
- **Features**: Range validation, deterministic vs creative output control

#### Task 4: Seed Parameter
- **File**: `task/4-task-seed.py`
- **Functionality**: Implemented seed parameter for deterministic output
- **Features**: Reproducible results, consistent responses with same inputs

#### Task 5: Max Tokens Parameter
- **File**: `task/5-task-max_tokens.py`
- **Functionality**: Implemented max_tokens parameter for response length control
- **Features**: Response truncation, token limit enforcement

#### Task 6: Frequency Penalty
- **File**: `task/6-task-frequency_penalty.py`
- **Functionality**: Implemented frequency_penalty parameter to reduce repetition
- **Features**: Token repetition reduction, content diversity enhancement

#### Task 7: Presence Penalty
- **File**: `task/7-task-presence_penalty.py`
- **Functionality**: Implemented presence_penalty parameter for topic diversity
- **Features**: Topic introduction encouragement, repetition reduction

#### Task 8: Stop Sequences
- **File**: `task/8-task-stop.py`
- **Functionality**: Implemented stop parameter for custom stop sequences
- **Features**: Custom sequence detection, response termination control

#### Task 9: Additional Parameters
- **File**: `task/9-task-additional-parameters.py`
- **Functionality**: Implemented support for additional parameters via custom_fields
- **Features**: DIAL Unified Protocol compliance, vendor-specific parameter support

### Core Architecture

#### Models Layer
- **Message Model**: Created `task/models/message.py` with a dataclass representing messages with role and content
- **Role Enum**: Implemented `task/models/role.py` with StrEnum for SYSTEM, USER, and AI roles
- **Conversation Model**: Developed `task/models/conversation.py` for managing conversation state and message history
- **Data Structure**: Established clean, type-hinted data models for all core entities

#### Application Layer
- **API Client**: Implemented `task/app/client.py` with comprehensive DIAL API communication
- **Main Application**: Created `task/app/main.py` for interactive chat functionality
- **Parameter Support**: Added extensive support for various LLM parameters with detailed documentation

## Supported Parameters

### 1. Temperature
Controls randomness in output. Lower values make responses more deterministic, while higher values increase creativity.

### 2. N (Number of Completions)
Specifies how many different completions to generate for a single prompt.

### 3. Seed
Provides deterministic output when reproducibility is required.

### 4. Max Tokens
Limits the length of the generated response.

### 5. Frequency Penalty
Reduces repetition by penalizing tokens that appear frequently in the text.

### 6. Presence Penalty
Reduces repetition by penalizing tokens that have appeared anywhere in the text.

### 7. Stop Sequences
Defines custom sequences that will cause the model to stop generating text.

## DIAL API Integration
The project uses the DIAL Unified Protocol, with custom parameters provided as:
```json
{
  "custom_fields": {
    "configuration": {
      "CUSTOM_PARAMETERS": "value"
    }
  }
}
```

## Testing Framework

### Comprehensive Test Suite
- **Temperature Tests**: `test/test_temperature.py` - Parametrized testing with different temperature values
- **N Parameter Tests**: `test/test_n.py` - Testing multiple completions generation
- **Models Tests**: `test/test_models.py` - Multi-model compatibility testing
- **Seed Tests**: `test/test_seed.py` - Deterministic output validation
- **Max Tokens Tests**: `test/test_max_tokens.py` - Response length control verification
- **Frequency Penalty Tests**: `test/test_frequency_penalty.py` - Repetition reduction validation
- **Presence Penalty Tests**: `test/test_presence_penalty.py` - Topic diversity testing
- **Stop Sequence Tests**: `test/test_stop.py` - Custom stop sequence validation
- **Additional Parameters Tests**: `test/test_additional_parameters.py` - Custom field parameter testing

#### Test Framework Features
- Dynamic module import for task files
- Parameterized testing for multiple values
- Response validation functions
- Error handling verification
- Cross-model compatibility checks

## Supported Models

The project has been tested and verified to work with the following models:
- gpt-4o
- gpt-4.1-nano-2025-04-14
- gpt-4.1-mini-2025-04-14
- gemini-2.0-flash-lite
- gemini-2.0-flash
- gemini-2.5-pro
- gemini-2.5-flash
- claude-3-5-haiku@20241022
- claude-3-7-sonnet@20250219
- claude-sonnet-4@20250514

## Usage Examples

### Interactive Chat
```bash
python -m task.app.main --model gpt-4o
```

### Parameter Testing
```bash
python -m task.2-task-n  # Test n parameter
python -m task.3-task-temperature  # Test temperature parameter
```

### Running Tests
```bash
python -m pytest ./test/ -v  # Run all tests
python -m pytest ./test/test_temperature.py -v  # Run specific test
```

## Technical Achievements

### 1. DIAL API Integration
- Successfully implemented DIAL API communication layer
- Added support for custom parameters via custom_fields
- Ensured compatibility with multiple LLM vendors

### 2. Parameter Support
- Comprehensive support for all major LLM parameters
- Proper range validation and error handling
- Detailed documentation for parameter effects

### 3. Cross-Model Compatibility
- Tested with multiple LLM providers (OpenAI, Google, Anthropic)
- Consistent interface across different models
- Model-specific parameter handling

### 4. Code Quality
- Type hints throughout the codebase
- Clean, modular architecture
- Comprehensive documentation and comments

## Project Completion Status

### Core Functionality ✅
- All parameter implementations completed
- API communication layer functional
- Model compatibility verified

### Testing Framework ✅
- All parameter tests implemented
- Cross-model compatibility tests
- Error handling verification

### Documentation ✅
- Architecture documentation
- Parameter guides
- Usage examples
- Testing strategy

### Infrastructure ✅
- Project structure established
- Dependencies managed
- Configuration system in place

## Key Outcomes

1. **Educational Value**: Successfully created a learning platform for understanding LLM parameters
2. **Technical Implementation**: Built a robust, extensible framework for LLM parameter experimentation
3. **Testing Coverage**: Established comprehensive test coverage for all implemented parameters
4. **Documentation**: Created detailed documentation for future development and maintenance
5. **Multi-Model Support**: Verified compatibility with multiple LLM providers and models

The project successfully meets its primary goal of providing a comprehensive implementation for working with different LLMs and their request parameters via the DIAL API, enabling developers to understand how various parameters affect LLM output and behavior.

## Requirements
- Python 3.11+
- DIAL API key
- EPAM VPN connection
- Dependencies listed in requirements.txt
