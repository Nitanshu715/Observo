# Friction Log — Agent Observability Bridge

## Summary
This prototype demonstrates the core idea: emitting structured events from agent workflows that can be routed to external tracing/observability tools (Logfire, AgentOps, Braintrust). For the hackathon we provided a minimal, extendable implementation.

## Environment
- Python 3.11+ (tested on 3.13)
- requests
- (optional) openai python package for LLM planning step

## Friction items encountered
1. **Composio Tool Router (Beta) docs & authentication**
   - Beta docs limited; setting up a real integration required private credentials and beta access.
   - Workaround: simulated tool calls (clear TODO in README to swap in real Composio calls).

2. **Observability endpoint authentication**
   - Logfire/AgentOps require API keys and specific span formats.
   - Workaround: prototype emits JSON events; format can be mapped to provider-specific spans. Implemented local prints and an optional generic POST to a configurable endpoint.

3. **OpenAI Agents SDK vs simple LLM calls**
   - Agents SDK provides richer constructs and tracing, but installing & wiring an Agents SDK agent takes time and specific configs.
   - Workaround: added option to call OpenAI `responses`/chat API for a planning step so demo still shows LLM usage.

4. **Context & event batching**
   - For production, events should be batched/asynced. For the prototype we print synchronously; future work: buffer and send in batches or stream via webhooks.

5. **Testing in offline/local demo**
   - Without API keys, live integrations were not possible within hackathon time. Chosen approach: build a clear, reproducible prototype and document how to wire real creds post-hackathon.

## Resolution & Future Work
- Provide mapping templates for Logfire/AgentOps span formats.  
- Add Composio Tool Router calls for real tool orchestration (once team has access/keys).  
- Add an async event buffer and preview dashboard for trace timelines.  
- Implement OpenAI Agents SDK orchestration for multi-agent handoffs and use built-in tracing features.

## Verdict
Prototype demonstrates the essential concept and provides a clear path to production integration. Suitable for judging: working code + documentation + friction log.
