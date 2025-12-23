# Available Models

DIAL API provides access to three major AI providers:

| Providers | Models |
|----------|--------|
| OpenAI | gpt-4o, gpt-4.1-mini-2025-04-14, gpt-4o-mini-2024-07-18 |
| Anthropic (Claude) | anthropic.claude-v3-haiku, claude-3-7-sonnet@20250219, claude-sonnet-4@20250514 |
| Google (Gemini) | gemini-2.5-pro, gemini-2.5-flash, gemini-2.0-flash-lite |

## Understanding Model Parameters

**stream**: Controls response delivery method
- Default: `false`
- When to use streaming: Real-time applications, chatbots, long responses
- When to use non-streaming: Batch processing, simple Q&A

**temperature**: Controls creativity vs. consistency
- Range: 0.0 to 2.0
- Default: 1.0
- Low values (0.0-0.3): Deterministic, factual responses
- Medium values (0.4-0.8): Balanced creativity and consistency
- High values (0.9-2.0): Very creative, unpredictable responses

**top_p**: (Nucleus Sampling) Alternative method to control randomness
- Range: 0.0 to 1.0
- Default: 1.0

How it works:
- `top_p: 0.1` = Consider only top 10% most likely tokens
- `top_p: 0.5` = Consider tokens making up 50% of probability mass
- `top_p: 1.0` = Consider all possible tokens

**Recommendation**: Use either `temperature` OR `top_p`, not both

**max_tokens**: Limits response length
- Default: No limit (model-dependent maximum)

Use cases:
- Short summaries: 50-100 tokens
- Detailed explanations: 500-1000 tokens
- Long-form content: 2000+ tokens

**presence_penalty**: Encourages discussing new topics
- Range: -2.0 to 2.0
- Default: 0.0
- Positive values: Encourage novelty and new topics
- Negative values: Allow more repetition of concepts
- How it works: Penalizes tokens that have appeared before (yes/no basis)

**Note**: This feature works only with OpenAI GPT models. According to the DIAL specification, you can use it with all models, but for those that do not support it, the parameter will be ignored.

**frequency_penalty**: Reduces repetitive word usage
- Range: -2.0 to 2.0
- Default: 0.0
- Positive values: Reduce word repetition
- Negative values: Increase word repetition
- How it works: Penalizes tokens proportionally to their frequency

**Note**: This feature works only with OpenAI GPT models. According to the DIAL specification, you can use it with all models, but for those that do not support it, the parameter will be ignored.

**stop**: Defines word of sentence when to stop generation

```json
{
    "stop": ["\n", "END", "###"]
}
```

```json
{
    "stop": "DIAL"
}
```

- Default: `null`

Use cases:
- Structured output (stop at specific markers)
- Dialogue systems (stop at speaker changes)
- List generation (stop at natural breaks)

**n**: Generate multiple response options
- Default: 1

Use cases:
- A/B testing different responses
- Providing multiple creative options
- Ensuring response quality through selection

**seed**: Ensures reproducible results

Use cases:
- Testing and debugging
- Consistent results across runs
- Research and experimentation

**Note**: This feature works only with OpenAI GPT and Gemini models. According to the DIAL specification, you can use it with all models, but for those that do not support it, the parameter will be ignored.

## Understanding DIAL API parameters allows you to:

- Control AI model behavior precisely
- Optimize for specific use cases
- Create consistent, high-quality outputs
- Experiment with different AI providers seamlessly

**The key to mastering these parameters is experimentation.** In the practice task you can experiment with different parameters and see their impact on the output.