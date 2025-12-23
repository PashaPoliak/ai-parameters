# LLM Parameters Guide

## Overview
This document provides detailed information about the various parameters available when working with Large Language Models through the DIAL API. Each parameter affects the model's output in different ways, and understanding their effects is crucial for fine-tuning model behavior for specific use cases.

## Parameter Details

### Temperature
- **Purpose**: Controls randomness in output
- **Range**: 0.0 to 2.0 (typically)
- **Default**: 1.0
- **Effect**: 
  - Lower values (e.g., 0.1) make responses more deterministic and focused
  - Higher values (e.g., 0.8-1.0) increase creativity and randomness
 - Value of 0 makes the model completely deterministic
- **Use Cases**: 
 - Low temperature for factual answers, coding, analysis
  - High temperature for creative writing, brainstorming

### N (Number of Completions)
- **Purpose**: Number of different completions to generate for a single prompt
- **Range**: 1 to maximum allowed by API
- **Default**: 1
- **Effect**: Generates multiple different responses to the same prompt
- **Use Cases**: Exploring multiple solution approaches, creative ideation

### Seed
- **Purpose**: Provides deterministic output when reproducibility is required
- **Range**: Integer values
- **Default**: None (non-deterministic)
- **Effect**: With the same seed, identical inputs will produce identical outputs
- **Use Cases**: Testing, debugging, scientific experiments requiring reproducibility

### Max Tokens
- **Purpose**: Limits the length of the generated response
- **Range**: 1 to maximum allowed by model
- **Default**: Varies by model
- **Effect**: Stops generation after specified token count
- **Use Cases**: Controlling response length, managing costs, fitting specific formats

### Frequency Penalty
- **Purpose**: Reduces repetition by penalizing tokens that appear frequently
- **Range**: -2.0 to 2.0
- **Default**: 0.0
- **Effect**: Higher values reduce repetition of the same tokens
- **Use Cases**: Long-form content, reducing repetitive phrases

### Presence Penalty
- **Purpose**: Reduces repetition by penalizing tokens that have appeared anywhere
- **Range**: -2.0 to 2.0
- **Default**: 0.0
- **Effect**: Higher values encourage the model to introduce new topics
- **Use Cases**: Diverse content generation, topic exploration

### Stop Sequences
- **Purpose**: Defines custom sequences that will cause the model to stop generating
- **Range**: Custom string sequences
- **Default**: Model-specific end-of-sequence tokens
- **Effect**: Generation stops when any of the specified sequences appear
- **Use Cases**: Custom response formatting, multi-part responses

## Parameter Interaction Effects

### Temperature + Top P
- Using both can have compounding effects on randomness
- Generally recommended to use only one of these parameters

### Temperature + Max Tokens
- Higher temperature with low max_tokens may result in less coherent short responses
- Lower temperature with high max_tokens may result in repetitive long responses

### Frequency Penalty + Presence Penalty
- Both can be used together to reduce repetition effectively
- High values of both may make responses too rigid or unnatural

## Best Practices

### For Creative Tasks
- Higher temperature (0.7-1.0)
- Consider using N > 1 to get multiple creative options
- Lower penalty values to allow creative flow

### For Analytical Tasks
- Lower temperature (0.1-0.3)
- Use seed for reproducible results
- Higher penalty values to maintain focus

### For Code Generation
- Low temperature (0.1-0.2)
- Use seed for reproducible results
- Careful max_tokens to avoid incomplete functions

### For Conversational Agents
- Medium temperature (0.4-0.7)
- Moderate penalty values to balance creativity and coherence
- Custom stop sequences for natural conversation flow

## DIAL API Specifics

### Custom Parameters
For parameters not directly supported in the DIAL API, use the custom_fields approach:

```json
{
  "custom_fields": {
    "configuration": {
      "reasoning_effort": "high",
      "thinking": true,
      "other_custom_parameter": "value"
    }
  }
}
```

### Model-Specific Parameters
Different models may support different parameter ranges or have different default behaviors. Always test parameters with your specific model.

## Testing Parameters

### A/B Testing Approach
1. Define your success metric (coherence, relevance, creativity, etc.)
2. Keep all parameters constant except the one being tested
3. Generate multiple samples with each parameter value
4. Evaluate results based on your metric
5. Document findings for future reference

### Parameter Combinations
- Test parameter interactions systematically
- Document combinations that work well for specific use cases
- Be aware that optimal combinations may vary by model and prompt