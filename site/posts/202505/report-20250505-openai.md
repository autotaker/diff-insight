---
date: '2025-05-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:59073f6...MicrosoftDocs:df7d67e
summary: 最近のリアルタイムオーディオのドキュメントには、重要な更新が含まれています。新機能として、音声活動検出の向上を図る「semantic_vad」が追加され、音声が終了したことをより自然に判断できるようになりました。また、WebRTCをサポートする新しいRealtime
  APIが「What's New」ドキュメントに掲載されており、これによりリアルタイムオーディオストリーミングが向上しました。互換性を破る変更は報告されていませんが、リファレンスドキュメントには新しいイベントに関する情報が追加され、開発者がAPIを効果的に活用するための手助けが強化されています。この更新は、ユーザーエクスペリエンスを向上させるための戦略的な変更といえます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:59073f6...MicrosoftDocs:df7d67e){target="_blank"}

# Highlights

リアルタイムオーディオのドキュメントにおける最近の変更は以下のような重要な更新を含んでいます。

## 新機能

1. **Semantic VADの追加**: 「semantic_vad」という新しいオプションがリアルタイムオーディオセッションに追加され、音声が終了したことを判断するための音声活動検出（VAD）機能が向上しました。

2. **WebRTC対応のRealtime API**: 「What's New」ドキュメントには、WebRTCをサポートする新しいRealtime APIのプレビュー機能が追加されました。これにより、リアルタイムオーディオストリーミングや低遅延のインタラクションが可能になります。

## 互換性を破る変更

- 特に互換性を破る変更は報告されていません。

## その他の更新

1. **リファレンスドキュメントの拡張**: クライアントおよびサーバー間の新しいイベントに関する情報がリファレンスドキュメントに追加されました。これにより、会話履歴からのアイテム取得や出力オーディオバッファのクリアの方法が明確になりました。

# Insights

リアルタイムオーディオのドキュメント更新は、ユーザーエクスペリエンスと開発者の使いやすさを向上させるための戦略的な変更です。

新たに追加された「semantic_vad」は、音声活動検出をより高度にすることにより、ユーザーの発話の終わりを自然に捉えることができます。これにより、リアルタイム音声インタラクションの品質が向上し、会話体験がよりスムーズになります。このアップデートは特に、迅速な応答が求められるアプリケーションで有用です。

また、「What's New」ドキュメントにおけるWebRTC対応のRealtime APIの追加は、技術的な進歩を示しています。WebRTCのサポートにより、開発者は高品質なリアルタイムオーディオ通信の実装が容易になり、多様なユースケースに対応可能です。例えば、リモートカスタマーサポートや音声アシスタントといった低遅延が必要なシナリオでの利用が想定されます。

さらに、リファレンスドキュメントのイベント情報の拡充により、開発者はAPIの機能をより深く理解し、それを効果的に活用できます。これにより、API統合の際の障壁が下がり、より良いユーザー体験の実現が可能になります。全体として、この一連の文書更新は、リアルタイムオーディオサービスの価値提案を強化するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [realtime-audio.md](#item-482ba3) | minor update | リアルタイムオーディオのVAD機能の強化 | modified | 12 | 3 | 15 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムオーディオリファレンスの拡張 | modified | 174 | 8 | 182 | 
| [whats-new.md](#item-53303b) | minor update | WebRTC対応のRealtime APIプレビュー機能追加 | modified | 4 | 0 | 4 | 


# Modified Contents
## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ Often, the first event sent by the caller on a newly established `/realtime` ses
 
 The [`session.update`](../realtime-audio-reference.md#realtimeclienteventsessionupdate) event can be used to configure the following aspects of the session:
 - Transcription of user input audio is opted into via the session's `input_audio_transcription` property. Specifying a transcription model (such as `whisper-1`) in this configuration enables the delivery of [`conversation.item.audio_transcription.completed`](../realtime-audio-reference.md#realtimeservereventconversationiteminputaudiotranscriptioncompleted) events.
-- Turn handling is controlled by the `turn_detection` property. This property's type can be set to `none` or `server_vad` as described in the [voice activity detection (VAD) and the audio buffer](#voice-activity-detection-vad-and-the-audio-buffer) section.
+- Turn handling is controlled by the `turn_detection` property. This property's type can be set to `none`, `semantic_vad`, or `server_vad` as described in the [voice activity detection (VAD) and the audio buffer](#voice-activity-detection-vad-and-the-audio-buffer) section.
 - Tools can be configured to enable the server to call out to external services or functions to enrich the conversation. Tools are defined as part of the `tools` property in the session configuration.
 
 An example `session.update` that configures several aspects of the session, including tools, follows. All session parameters are optional and can be omitted if not needed.
@@ -144,9 +144,12 @@ You can also construct a custom context that the model uses outside of the sessi
 
 The server maintains an input audio buffer containing client-provided audio that hasn't yet been committed to the conversation state.
 
-One of the key [session-wide](#session-configuration) settings is `turn_detection`, which controls how data flow is handled between the caller and model. The `turn_detection` setting can be set to `none` or `server_vad` (to use [server-side voice activity detection](#server-decision-mode)).
+One of the key [session-wide](#session-configuration) settings is `turn_detection`, which controls how data flow is handled between the caller and model. The `turn_detection` setting can be set to `none`, `semantic_vad`, or `server_vad` (to use [server-side voice activity detection](#server-decision-mode)).
 
-By default, voice activity detection (VAD) is enabled, and the server automatically generates responses when it detects the end of speech in the input audio buffer. You can change the behavior by setting the `turn_detection` property in the session configuration.
+- `server_vad`: Automatically chunks the audio based on periods of silence.
+- `semantic_vad`: Chunks the audio when the model believes based on the words said by the user that they have completed their utterance.
+
+By default, server VAD (`server_vad`) is enabled, and the server automatically generates responses when it detects the end of speech in the input audio buffer. You can change the behavior by setting the `turn_detection` property in the session configuration.
 
 ### Without server decision mode
 
@@ -201,6 +204,12 @@ sequenceDiagram
     Server->>Client: conversation.item.created
 -->
 
+### Semantic VAD
+
+Semantic VAD detects when the user has finished speaking based on the words they have uttered. The input audio is scored based on the probability that the user is done speaking. When the probability is low the model will wait for a timeout. When the probability is high there's no need to wait. 
+
+With the (`semantic_vad`) mode, the model is less likely to interrupt the user during a speech-to-speech conversation, or chunk a transcript before the user is done speaking.
+
 ### VAD without automatic response generation
 
 You can use server-side voice activity detection (VAD) without automatic response generation. This approach can be useful when you want to implement some degree of moderation. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオのVAD機能の強化"
}
```

### Explanation
この変更では、リアルタイムオーディオセッションの設定における「turn_detection」プロパティのオプションが拡張されました。具体的には、新たに「semantic_vad」という選択肢が追加され、従来の「none」と「server_vad」に加え、音声が終了したと仮定する際のユーザーの発話に基づいて音声を分割することが可能になりました。この機能により、モデルはユーザーが話し終わるタイミングをより正確に判断でき、会話をよりスムーズに進めることができます。

加えて、ドキュメント内に「semantic VAD」に関するセクションが新たに設けられ、ユーザーが発話を終える確率に応じた挙動の説明が追加されました。このように、音声活動検出（VAD）機能が改善されることで、リアルタイムオーディオセッションにおける操作性が向上します。全体として、ユーザー体験を向上させるためのマイナーな更新となっています。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -30,10 +30,12 @@ There are nine client events that can be sent from the client to the server:
 |-------|-------------|
 | [RealtimeClientEventConversationItemCreate](#realtimeclienteventconversationitemcreate) | The client `conversation.item.create` event is used to add a new item to the conversation's context, including messages, function calls, and function call responses. |
 | [RealtimeClientEventConversationItemDelete](#realtimeclienteventconversationitemdelete) | The client `conversation.item.delete` event is used to remove an item from the conversation history. |
+| [RealtimeClientEventConversationItemRetrieve](#realtimeclienteventconversationitemretrieve) | The client `conversation.item.retrieve` event is used to retrieve an item from the conversation history. |
 | [RealtimeClientEventConversationItemTruncate](#realtimeclienteventconversationitemtruncate) | The client `conversation.item.truncate` event is used to truncate a previous assistant message's audio. |
 | [RealtimeClientEventInputAudioBufferAppend](#realtimeclienteventinputaudiobufferappend) | The client `input_audio_buffer.append` event is used to append audio bytes to the input audio buffer. |
 | [RealtimeClientEventInputAudioBufferClear](#realtimeclienteventinputaudiobufferclear) | The client `input_audio_buffer.clear` event is used to clear the audio bytes in the buffer. |
 | [RealtimeClientEventInputAudioBufferCommit](#realtimeclienteventinputaudiobuffercommit) | The client `input_audio_buffer.commit` event is used to commit the user input audio buffer. |
+| [RealtimeClientEventOutputAudioBufferClear](#realtimeclienteventoutputaudiobufferclear) | The client `output_audio_buffer.clear` event is used to clear the audio bytes in the output buffer.<br/><br/>This event is only applicable for WebRTC. |
 | [RealtimeClientEventResponseCancel](#realtimeclienteventresponsecancel) | The client `response.cancel` event is used to cancel an in-progress response. |
 | [RealtimeClientEventResponseCreate](#realtimeclienteventresponsecreate) | The client `response.create` event is used to instruct the server to create a response via model inferencing. |
 | [RealtimeClientEventSessionUpdate](#realtimeclienteventsessionupdate) | The client `session.update` event is used to update the session's default configuration. |
@@ -83,6 +85,31 @@ The server responds with a `conversation.item.deleted` event, unless the item do
 | type | string | The event type must be `conversation.item.delete`. |
 | item_id | string | The ID of the item to delete. | 
 
+
+### RealtimeClientEventConversationItemRetrieve
+
+The client `conversation.item.retrieve` event is used to retrieve the server's representation of a specific item in the conversation history. This event is useful, for example, to inspect user audio after noise cancellation and VAD. 
+
+If the client event is successful, the server responds with a `conversation.item.retrieved` event. If the item doesn't exist in the conversation history, the server will respond with an error.
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.retrieve",
+  "item_id": "<item_id>",
+  "event_id": "<event_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.retrieve`. | 
+| item_id | string | The ID of the item to retrieve. | 
+| event_id | string | The ID of the event. |
+
 ### RealtimeClientEventConversationItemTruncate
 
 The client `conversation.item.truncate` event is used to truncate a previous assistant message's audio. The server produces audio faster than realtime, so this event is useful when the user interrupts to truncate audio that was sent to the client but not yet played. The server's understanding of the audio with the client's playback is synchronized.
@@ -179,6 +206,32 @@ The server responds with an `input_audio_buffer.committed` event.
 |-------|------|-------------| 
 | type | string | The event type must be `input_audio_buffer.commit`. | 
 
+### RealtimeClientEventOutputAudioBufferClear
+
+The client `output_audio_buffer.clear` event is used to clear the audio bytes in the buffer. 
+
+> [!NOTE]
+> This event is only applicable for WebRTC. 
+
+This event should be preceded by a `response.cancel` client event to stop the generation of the current response.
+
+The server stops generating audio and responds with an `output_audio_buffer.cleared` event.
+
+#### Event structure
+
+```json
+{
+  "type": "output_audio_buffer.clear"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | 
+|-------|------|-------------| 
+| event_id | string | The ID of the event that caused the error. |
+| type | string | The event type must be `output_audio_buffer.clear`. | 
+
 ### RealtimeClientEventResponseCancel
 
 The client `response.cancel` event is used to cancel an in-progress response. 
@@ -257,6 +310,7 @@ There are 28 server events that can be received from the server:
 |-------|-------------|
 | [RealtimeServerEventConversationCreated](#realtimeservereventconversationcreated) | The server `conversation.created` event is returned right after session creation. One conversation is created per session. |
 | [RealtimeServerEventConversationItemCreated](#realtimeservereventconversationitemcreated) | The server `conversation.item.created` event is returned when a conversation item is created. |
+| [RealtimeServerEventConversationItemRetrieved](#realtimeservereventconversationitemretrieved) | The server `conversation.item.retrieved` event is returned when a conversation item is retrieved. |
 | [RealtimeServerEventConversationItemDeleted](#realtimeservereventconversationitemdeleted) | The server `conversation.item.deleted` event is returned when the client deleted an item in the conversation with a `conversation.item.delete` event. |
 | [RealtimeServerEventConversationItemInputAudioTranscriptionCompleted](#realtimeservereventconversationiteminputaudiotranscriptioncompleted) | The server `conversation.item.input_audio_transcription.completed` event is the result of audio transcription for speech written to the audio buffer. |
 | [RealtimeServerEventConversationItemInputAudioTranscriptionFailed](#realtimeservereventconversationiteminputaudiotranscriptionfailed) | The server `conversation.item.input_audio_transcription.failed` event is returned when input audio transcription is configured, and a transcription request for a user message failed. |
@@ -266,6 +320,9 @@ There are 28 server events that can be received from the server:
 | [RealtimeServerEventInputAudioBufferCommitted](#realtimeservereventinputaudiobuffercommitted) | The server `input_audio_buffer.committed` event is returned when an input audio buffer is committed, either by the client or automatically in server VAD mode. |
 | [RealtimeServerEventInputAudioBufferSpeechStarted](#realtimeservereventinputaudiobufferspeechstarted) | The server `input_audio_buffer.speech_started` event is returned in `server_vad` mode when speech is detected in the audio buffer. |
 | [RealtimeServerEventInputAudioBufferSpeechStopped](#realtimeservereventinputaudiobufferspeechstopped) | The server `input_audio_buffer.speech_stopped` event is returned in `server_vad` mode when the server detects the end of speech in the audio buffer. |
+| [RealtimeServerEventOutputAudioBufferCleared](#realtimeservereventoutputaudiobuffercleared) | The server `output_audio_buffer.cleared` event is returned when the user has interrupted (`input_audio_buffer.speech_started`), or when the client has emitted the `output_audio_buffer.clear` event to manually cut off the current audio response.<br/><br/>This event is only applicable for WebRTC. |
+| [RealtimeServerEventOutputAudioBufferStarted](#realtimeservereventoutputaudiobufferstarted) | The server `output_audio_buffer.started` event is returned when the server begins streaming audio to the client. This event is emitted after an audio content part has been added (`response.content_part.added`) to the response.<br/><br/>This event is only applicable for WebRTC. |
+| [RealtimeServerEventOutputAudioBufferStopped](#realtimeservereventoutputaudiobufferstopped) | The server `output_audio_buffer.stopped` event is returned when the output audio buffer has been completely drained on the server, and no more audio is forthcoming.<br/><br/>This event is only applicable for WebRTC. |
 | [RealtimeServerEventRateLimitsUpdated](#realtimeservereventratelimitsupdated) | The server `rate_limits.updated` event is emitted at the beginning of a response to indicate the updated rate limits. |
 | [RealtimeServerEventResponseAudioDelta](#realtimeservereventresponseaudiodelta) | The server `response.audio.delta` event is returned when the model-generated audio is updated. |
 | [RealtimeServerEventResponseAudioDone](#realtimeservereventresponseaudiodone) | The server `response.audio.done` event is returned when the model-generated audio is done. |
@@ -338,6 +395,27 @@ The server `conversation.item.created` event is returned when a conversation ite
 | previous_item_id | string | The ID of the preceding item in the conversation context, allows the client to understand the order of the conversation. | 
 | item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) | The item that was created. |
 
+### RealtimeServerEventConversationItemRetrieved
+
+The server `conversation.item.retrieved` event is returned when a conversation item is retrieved. 
+
+#### Event structure
+
+```json
+{
+  "type": "conversation.item.retrieved",
+  "previous_item_id": "<previous_item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.retrieved`. | 
+| event_id | string | The ID of the event. |
+| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) | The item that was retrieved. |
+
 ### RealtimeServerEventConversationItemDeleted
 
 The server `conversation.item.deleted` event is returned when the client deleted an item in the conversation with a `conversation.item.delete` event. This event is used to synchronize the server's understanding of the conversation history with the client's view.
@@ -575,6 +653,83 @@ The server also sends a `conversation.item.created` event with the user message
 | audio_end_ms | integer | Milliseconds since the session started when speech stopped. This property corresponds to the end of audio sent to the model, and thus includes the `min_silence_duration_ms` configured in the session. | 
 | item_id | string | The ID of the user message item created. | 
 
+### RealtimeServerEventOutputAudioBufferCleared
+
+The server `output_audio_buffer.cleared` event is returned when the output audio buffer is cleared. 
+
+> [!NOTE]
+> This event is only applicable for WebRTC. 
+
+This happens either in VAD mode when the user has interrupted (`input_audio_buffer.speech_started`), or when the client has emitted the `output_audio_buffer.clear` event to manually cut off the current audio response. 
+
+#### Event structure
+
+```json
+{
+  "type": "output_audio_buffer.cleared"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `output_audio_buffer.cleared`. | 
+| event_id | string | The ID of the server event. |
+| response_id | string | The unique ID of the response that produced the audio. |
+
+### RealtimeServerEventOutputAudioBufferStarted
+
+The server `output_audio_buffer.started` event is returned when the server begins streaming audio to the client. This event is emitted after an audio content part has been added (`response.content_part.added`) to the response.
+
+> [!NOTE]
+> This event is only applicable for WebRTC. 
+
+#### Event structure
+
+```json
+{
+  "type": "output_audio_buffer.started",
+  "event_id": "<item_id>",
+  "response_id": "<response_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `output_audio_buffer.started`. | 
+| event_id | string | The ID of the server event. |
+| response_id | string | The unique ID of the response that produced the audio. |
+
+### RealtimeServerEventOutputAudioBufferStopped
+
+The server `output_audio_buffer.stopped` event is returned when the output audio buffer has been completely drained on the server, and no more audio is forthcoming. 
+
+> [!NOTE]
+> This event is only applicable for WebRTC. 
+
+This event is returned after the full response data has been sent to the client via the `response.done` event.
+
+#### Event structure
+
+```json
+{
+  "type": "output_audio_buffer.stopped",
+  "audio_end_ms": 0,
+  "item_id": "<item_id>"
+}
+```
+
+#### Properties
+
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `output_audio_buffer.stopped`. | 
+| event_id | string | The ID of the server event. |
+| response_id | string | The unique ID of the response that produced the audio. |
+
 ### RealtimeServerEventRateLimitsUpdated
 
 The server `rate_limits.updated` event is emitted at the beginning of a response to indicate the updated rate limits. 
@@ -1048,8 +1203,15 @@ The server `session.updated` event is returned when a session is updated by the
 
 | Field | Type | Description | 
 |-------|------|-------------|
-| model | [RealtimeAudioInputTranscriptionModel](#realtimeaudioinputtranscriptionmodel) | The `whisper-1` model is currently the default model supported for audio input transcription. | 
+| language | string | The language of the input audio. Supplying the input language in ISO-639-1 format (such as `en`) will improve accuracy and latency. |
+| model | [RealtimeAudioInputTranscriptionModel](#realtimeaudioinputtranscriptionmodel) | The model for audio input transcription. For example, `whisper-1`. |
+| prompt | string | The prompt for the audio input transcription. Optional text to guide the model's style or continue a previous audio segment. For the `whisper-1` model, the prompt is a list of keywords. For the `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` models, the prompt is a free text string such as "expect words related to technology."|
 
+### RealtimeAudioInputAudioNoiseReductionSettings
+
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | Type of noise reduction. Specify `near_field` for close-talking microphones such as headphones or `far_field` for far-field microphones such as laptop or conference room microphones. | 
 
 ### RealtimeClientEvent
 
@@ -1227,8 +1389,9 @@ You use the `RealtimeRequestSession` object when you want to update the session
 | instructions | string | The instructions (the system message) to guide the model's text and audio responses.<br><br>Here are some example instructions to help guide content and format of text and audio responses:<br>`"instructions": "be succinct"`<br>`"instructions": "act friendly"`<br>`"instructions": "here are examples of good responses"`<br><br>Here are some example instructions to help guide audio behavior:<br>`"instructions": "talk quickly"`<br>`"instructions": "inject emotion into your voice"`<br>`"instructions": "laugh frequently"`<br><br>While the model might not always follow these instructions, they provide guidance on the desired behavior. |
 | voice | [RealtimeVoice](#realtimevoice) | The voice used for the model response for the session.<br><br>Once the voice is used in the session for the model's audio response, it can't be changed. | 
 | input_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the input audio. | 
-| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the output audio. | 
-| input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) | The settings for audio input transcription.<br><br>This property is nullable. |
+| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the output audio. |
+| input_audio_noise_reduction | boolean | Configuration for input audio noise reduction. This can be set to null to turn off. Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model. Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.<br><br>This property is nullable.| 
+| input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) | The configuration for input audio transcription. The configuration is null (off) by default. Input audio transcription isn't native to the model, since the model consumes audio directly. Transcription runs asynchronously through the `/audio/transcriptions` endpoint and should be treated as guidance of input audio content rather than precisely what the model heard. For additional guidance to the transcription service, the client can optionally set the language and prompt for transcription.<br><br>This property is nullable. |
 | turn_detection | [RealtimeTurnDetection](#realtimeturndetection) | The turn detection settings for the session.<br><br>This property is nullable. |
 | tools | array of [RealtimeTool](#realtimetool) | The tools available to the model for the session. |
 | tool_choice | [RealtimeToolChoice](#realtimetoolchoice) | The tool choice for the session.<br><br>Allowed values: `auto`, `none`, and `required`. Otherwise, you can specify the name of the function to use. |
@@ -1493,17 +1656,20 @@ Currently, only 'function' tools are supported.
 
 | Field | Type | Description | 
 |-------|------|-------------|
-| type | [RealtimeTurnDetectionType](#realtimeturndetectiontype) | The type of turn detection.<br><br>Allowed values: `server_vad` |
-| threshold | number | The activation threshold for the server VAD turn detection. In noisy environments, you might need to increase the threshold to avoid false positives. In quiet environments, you might need to decrease the threshold to avoid false negatives.<br><br>Defaults to `0.5`. You can set the threshold to a value between `0.0` and `1.0`. |
-| prefix_padding_ms | string | The duration of speech audio (in milliseconds) to include before the start of detected speech.<br><br>Defaults to `300` milliseconds. |
-| silence_duration_ms | string | The duration of silence (in milliseconds) to detect the end of speech. You want to detect the end of speech as soon as possible, but not too soon to avoid cutting off the last part of the speech.<br><br>The model will respond more quickly if you set this value to a lower number, but it might cut off the last part of the speech. If you set this value to a higher number, the model will wait longer to detect the end of speech, but it might take longer to respond.<br><br>Defaults to `500` milliseconds. |
+| type | [RealtimeTurnDetectionType](#realtimeturndetectiontype) | The type of turn detection.<br><br>Allowed values: `semantic_vad` or `server_vad` |
+| threshold | number | The activation threshold for the server VAD (`server_vad`) turn detection. In noisy environments, you might need to increase the threshold to avoid false positives. In quiet environments, you might need to decrease the threshold to avoid false negatives.<br><br>Defaults to `0.5`. You can set the threshold to a value between `0.0` and `1.0`.<br/><br>This property is only applicable for `server_vad` turn detection. |
+| prefix_padding_ms | string | The duration of speech audio (in milliseconds) to include before the start of detected speech.<br><br>Defaults to `300` milliseconds.<br/><br>This property is only applicable for `server_vad` turn detection. |
+| silence_duration_ms | string | The duration of silence (in milliseconds) to detect the end of speech. You want to detect the end of speech as soon as possible, but not too soon to avoid cutting off the last part of the speech.<br><br>The model will respond more quickly if you set this value to a lower number, but it might cut off the last part of the speech. If you set this value to a higher number, the model will wait longer to detect the end of speech, but it might take longer to respond.<br><br>Defaults to `500` milliseconds.<br/><br>This property is only applicable for `server_vad` turn detection. |
 | create_response | boolean | Indicates whether the server will automatically create a response when VAD is enabled and speech stops.<br><br>Defaults to `true`. |
+| interrupt_response | boolean | Indicates whether the server will automatically interrupt any ongoing response with output to the default (`auto`) conversation when a VAD start event occurs.<br><br>Defaults to `true`. |
+| eagerness | boolean | The eagerness of the model to respond and interrupt the user. Specify `low` to wait longer for the user to continue speaking. Specify `high` to chunk the audio as soon as possible for quicker responses. The default value is `auto` that's equivalent to medium.<br/><br>This property is only applicable for `server_vad` turn detection. |
 
 ### RealtimeTurnDetectionType
 
 **Allowed Values:**
 
-* `server_vad` 
+* `semantic_vad` - Semantic VAD detects when the user has finished speaking based on the words they have uttered. The input audio is scored based on the probability that the user is done speaking. When the probability is low the model will wait for a timeout. When the probability is high there's no need to wait. 
+* `server_vad` - The server evaluates user audio from the client. The server automatically uses that audio to initiate response generation on applicable conversations when an end of speech is detected.
 
 ### RealtimeVoice
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオリファレンスの拡張"
}
```

### Explanation
この変更では、リアルタイムオーディオのリファレンスドキュメントが拡張され、クライアントおよびサーバー間のイベントに関する情報が追加されました。新たに「RealtimeClientEventConversationItemRetrieve」および「RealtimeClientEventOutputAudioBufferClear」といったイベントが導入され、特に会話履歴から特定のアイテムを取得したり、出力オーディオバッファをクリアしたりするための明確なメソッドが提供されました。

また、イベントに伴う構造やプロパティに関する詳細な説明が追加され、ユーザーがどのようにこれらのイベントを活用できるかを理解しやすくなっています。特に、「semantic_vad」や「server_vad」を用いたターン検出の実装が強調され、これらの機能がどのようにオーディオのインタラクションを改善するかについての情報も提供されています。

その結果、ユーザーはこのリアルタイムオーディオサービスをより効率的に利用できるようになるため、全体的にドキュメントの価値が向上しています。この変更は、特に開発者がAPIを統合する際に役立つ情報を提供することで、より良い体験を実現します。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -21,6 +21,10 @@ This article provides a summary of the latest releases and major documentation u
 
 ## April 2025
 
+### Realtime API (preview) support for WebRTC
+
+The Realtime API (preview) now supports WebRTC, enabling real-time audio streaming and low-latency interactions. This feature is ideal for applications requiring immediate feedback, such as live customer support or interactive voice assistants. For more information, see the [Realtime API (preview) documentation](./how-to/realtime-audio-webrtc.md).
+
 ### GPT-image-1 released (preview, limited access)
 
 GPT-image-1 (2025-04-15) is the latest image generation model from Azure OpenAI. It features major improvements over DALL-E, including:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "WebRTC対応のRealtime APIプレビュー機能追加"
}
```

### Explanation
この変更では、「What's New」ドキュメントに新しい機能としてWebRTCをサポートするRealtime API（プレビュー）が追加されました。この新機能により、リアルタイムオーディオストリーミングおよび低遅延のインタラクションが可能になります。特に、リアルタイムでのフィードバックが求められるアプリケーションに最適です。例えば、ライブカスタマーサポートやインタラクティブ音声アシスタントなど、多様なユースケースに対応しています。

また、この新機能に関する詳細な情報を得るためのリンクが追加されており、ユーザーはより具体的な実装ガイドや使い方を参照することができます。このアップデートは、開発者やエンドユーザーに最新の機能を知ってもらうための重要な情報を提供しており、全体的なドキュメントの有用性を向上させています。


