---
date: '2024-12-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a72151d...MicrosoftDocs:b8144fb
summary: この変更では、リアルタイムAPIに関するドキュメントが大幅に更新され、新しい図や画像が追加されました。特に、WebSocket接続や音声活動検出（VAD）に関する説明が強化され、イベント処理やセッション管理の流れが詳細に記載されています。また、古くなった画像が削除され、最新の情報提供が進められています。これにより、ユーザーはAPIの使い方やデータフローをより直感的に理解できるようになりました。全体として、ドキュメントの整合性と正確さが向上し、ユーザーにとっての価値が高まっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a72151d...MicrosoftDocs:b8144fb){target="_blank"}

# ハイライト

この変更では、リアルタイムAPIに関するドキュメントが大幅に更新され、新しい図や画像を多く追加しました。特に、WebSocket接続や音声活動検出（VAD）に関する説明が強化され、イベント処理やセッション管理の流れが詳細に記載されています。また、古くなった画像ファイルが削除され、新しい情報の提供が進められています。

## 新機能
- リアルタイムAPIに関連する新しい図や画像が追加され、APIの使用やデータフローが視覚的にわかりやすくなっています。
  - WebSocketを用いた認証とデータフロー
  - 音声活動検出を利用したサーバーサイドの処理

## 破壊的変更
- 特定の機能やビジュアル資料は削除されましたが、これが直接的な破壊的変更とは考えられません。ただし、ユーザーが古い情報にアクセスするリスクを減らす調整は行われています。

## その他の更新
- JavaScript関連のリンクが最新の情報を指すように更新され、ドキュメントの整合性と正確さが向上しました。

# 洞察

このドキュメントの更新は、リアルタイムAPIの利用をよりスムーズにするために行われた重要なステップです。新たに追加された図や視覚資料は、開発者にとって複雑な音声データ処理を直感的に理解するための手助けとなります。特に、WebSocketを使ったリアルタイム通信や音声データのバッファリングと処理、さらには音声活動検出（VAD）の利用により、より高度な音声インターフェースの実装が可能になっています。

また、古くなった画像の削除やリンクの更新により、ユーザーに提供される情報が常に最新で関連性のあるものとなるよう維持されています。このように視覚資料やコンテンツが改善されることで、ドキュメント全体の価値が向上し、ユーザーの理解を深めると同時に、技術的な実装の成功をサポートする基盤を提供しています。

これらの変更は、APIや関連技術が進化する中、最新の情報と方法に基づいた確実なサポートを提供するための継続的な努力の一環であるといえます。今後も技術進化に合わせた更新が期待され、ユーザーはますます高品質な開発経験を享受できるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [realtime-audio.md](#item-482ba3) | minor update | リアルタイムAPIの更新と構成 | modified | 129 | 17 | 146 | 
| [create-batch-job.png](#item-fd1371) | minor update | バッチジョブ作成画像の削除 | removed | 0 | 0 | 0 | 
| [conversation-item-sequence.png](#item-4caf37) | minor update | 会話アイテムシーケンス画像の追加 | added | 0 | 0 | 0 | 
| [input-audio-buffer-client-managed.png](#item-07f39e) | minor update | クライアント管理の入力音声バッファ画像の追加 | added | 0 | 0 | 0 | 
| [input-audio-buffer-server-vad.png](#item-223de3) | minor update | サーバーVADの入力音声バッファ画像の追加 | added | 0 | 0 | 0 | 
| [realtime-api-sequence.png](#item-af9ae0) | minor update | リアルタイムAPIシーケンス画像の追加 | added | 0 | 0 | 0 | 
| [deployments-new.png](#item-23a410) | minor update | モデルのデプロイメント画像の削除 | removed | 0 | 0 | 0 | 
| [azure-openai-studio-playground.png](#item-754487) | minor update | Azure OpenAI スタジオのプレイグラウンド画像の削除 | removed | 0 | 0 | 0 | 
| [quota.png](#item-9e5234) | minor update | プロビジョニングのクオータ画像の削除 | removed | 0 | 0 | 0 | 
| [dall-e-studio-new.png](#item-136e43) | minor update | DALL-E スタジオの新しい画像の削除 | removed | 0 | 0 | 0 | 
| [studio-vision-enhanced-video.png](#item-a59d96) | minor update | スタジオビジョンの強化動画の画像削除 | removed | 0 | 0 | 0 | 
| [studio-vision-enhanced.png](#item-4282af) | minor update | スタジオビジョンの強化画像の削除 | removed | 0 | 0 | 0 | 
| [studio-vision.png](#item-a5dbbb) | minor update | スタジオビジョン画像の削除 | removed | 0 | 0 | 0 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムオーディオリファレンスの更新 | modified | 496 | 482 | 978 | 
| [toc.yml](#item-c945af) | minor update | JavaScriptリンクの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/how-to/realtime-audio.md{#item-482ba3}

<details>
<summary>Diff</summary>
````diff
@@ -85,31 +85,54 @@ To authenticate:
 
 ## Realtime API architecture
 
-Once the WebSocket connection session to `/realtime` is established and authenticated, the functional interaction takes place via events for sending and receiving WebSocket messages. These events each take the form of a JSON object. Events can be sent and received in parallel and applications should generally handle them both concurrently and asynchronously.
-
-- A caller establishes a connection to `/realtime`, which starts a new `session`.
+Once the WebSocket connection session to `/realtime` is established and authenticated, the functional interaction takes place via events for sending and receiving WebSocket messages. These events each take the form of a JSON object. 
+
+:::image type="content" source="../media/how-to/real-time/realtime-api-sequence.png" alt-text="Diagram of the Realtime API authentication and connection sequence." lightbox="../media/how-to/real-time/realtime-api-sequence.png":::
+
+<!--
+sequenceDiagram
+  actor User as End User
+  participant MiddleTier as /realtime host
+  participant AOAI as Azure OpenAI
+  User->>MiddleTier: Begin interaction
+  MiddleTier->>MiddleTier: Authenticate/Validate User
+  MiddleTier--)User: audio information
+  User--)MiddleTier: 
+  MiddleTier--)User: text information
+  User--)MiddleTier: 
+  MiddleTier--)User: control information
+  User--)MiddleTier: 
+  MiddleTier->>AOAI: connect to /realtime
+  MiddleTier->>AOAI: configure session
+  AOAI->>MiddleTier: session start
+  MiddleTier--)AOAI: send/receive WS commands
+  AOAI--)MiddleTier: 
+  AOAI--)MiddleTier: create/start conversation responses
+  AOAI--)MiddleTier: (within responses) create/start/add/finish items
+  AOAI--)MiddleTier: (within items) create/stream/finish content parts
+-->
+
+Events can be sent and received in parallel and applications should generally handle them both concurrently and asynchronously.
+
+- A client-side caller establishes a connection to `/realtime`, which starts a new [`session`](#session-configuration).
 - A `session` automatically creates a default `conversation`. Multiple concurrent conversations aren't supported.
-- The `conversation` accumulates input signals until a `response` is started, either via a direct event by the caller or automatically by voice-activity-based (VAD) turn detection.
+- The `conversation` accumulates input signals until a `response` is started, either via a direct event by the caller or automatically by voice activity detection (VAD).
 - Each `response` consists of one or more `items`, which can encapsulate messages, function calls, and other information.
 - Each message `item` has `content_part`, allowing multiple modalities (text and audio) to be represented across a single item.
 - The `session` manages configuration of caller input handling (for example, user audio) and common output generation handling.
-- Each caller-initiated `response.create` can override some of the output `response` behavior, if desired.
+- Each caller-initiated [`response.create`](../realtime-audio-reference.md#realtimeclienteventresponsecreate) can override some of the output [`response`](../realtime-audio-reference.md#realtimeresponse) behavior, if desired.
 - Server-created `item` and the `content_part` in messages can be populated asynchronously and in parallel. For example, receiving audio, text, and function information concurrently in a round robin fashion.
 
-## Session configuration and turn handling mode
-
-Often, the first event sent by the caller on a newly established `/realtime` session is a `session.update` payload. This event controls a wide set of input and output behavior, with output and response generation portions then later overridable via `response.create` properties.
-
-One of the key session-wide settings is `turn_detection`, which controls how data flow is handled between the caller and model:
+## Session configuration
 
-- `server_vad` evaluates incoming user audio (as sent via `input_audio_buffer.append`) using a voice activity detector (VAD) component and automatically use that audio to initiate response generation on applicable conversations when an end of speech is detected. Silence detection for the VAD can be configured when specifying `server_vad` detection mode.
-- `none` relies on caller-initiated `input_audio_buffer.commit` and `response.create` events to progress conversations and produce output. This setting is useful for push-to-talk applications or situations that have external audio flow control (such as caller-side VAD component). These manual signals can still be used in `server_vad` mode to supplement VAD-initiated response generation.
+Often, the first event sent by the caller on a newly established `/realtime` session is a [`session.update`](../realtime-audio-reference.md#realtimeclienteventsessionupdate) payload. This event controls a wide set of input and output behavior, with output and response generation properties then later overridable using the [`response.create`](../realtime-audio-reference.md#realtimeclienteventresponsecreate) event.
 
-Transcription of user input audio is opted into via the `input_audio_transcription` property. Specifying a transcription model (`whisper-1`) in this configuration enables the delivery of `conversation.item.audio_transcription.completed` events.
+The [`session.update`](../realtime-audio-reference.md#realtimeclienteventsessionupdate) event can be used to configure the following aspects of the session:
+- Transcription of user input audio is opted into via the session's `input_audio_transcription` property. Specifying a transcription model (`whisper-1`) in this configuration enables the delivery of [`conversation.item.audio_transcription.completed`](../realtime-audio-reference.md#realtimeservereventconversationiteminputaudiotranscriptioncompleted) events.
+- Turn handling is controlled by the `turn_detection` property. This property can be set to `none` or `server_vad` as described in the [input audio buffer and turn handling](#input-audio-buffer-and-turn-handling) section.
+- Tools can be configured to enable the server to call out to external services or functions to enrich the conversation. Tools are defined as part of the `tools` property in the session configuration.
 
-### Session update example
-
-An example `session.update` that configures several aspects of the session, including tools, follows. All session parameters are optional; not everything needs to be configured!
+An example `session.update` that configures several aspects of the session, including tools, follows. All session parameters are optional and can be omitted if not needed.
 
 ```json
 {
@@ -136,7 +159,7 @@ An example `session.update` that configures several aspects of the session, incl
           "properties": {
             "location": {
               "type": "string",
-              "description": "The city and state e.g. San Francisco, CA"
+              "description": "The city and state such as San Francisco, CA"
             },
             "unit": {
               "type": "string",
@@ -157,6 +180,95 @@ An example `session.update` that configures several aspects of the session, incl
 }
 ```
 
+## Input audio buffer and turn handling
+
+The server maintains an input audio buffer containing client-provided audio that has not yet been committed to the conversation state.
+
+One of the key [session-wide](#session-configuration) settings is `turn_detection`, which controls how data flow is handled between the caller and model. The `turn_detection` setting can be set to `none` or `server_vad` (to use [server-side voice activity detection](#server-decision-mode)).
+
+### Without server decision mode
+
+By default, the session is configured with the `turn_detection` type effectively set to `none`. 
+
+The session relies on caller-initiated [`input_audio_buffer.commit`](../realtime-audio-reference.md#realtimeclienteventinputaudiobuffercommit) and [`response.create`](../realtime-audio-reference.md#realtimeclienteventresponsecreate) events to progress conversations and produce output. This setting is useful for push-to-talk applications or situations that have external audio flow control (such as caller-side VAD component). These manual signals can still be used in `server_vad` mode to supplement VAD-initiated response generation.
+
+- The client can append audio to the buffer by sending the [`input_audio_buffer.append`](../realtime-audio-reference.md#realtimeclienteventinputaudiobufferappend) event.
+- The client commits the input audio buffer by sending the [`input_audio_buffer.commit`](../realtime-audio-reference.md#realtimeclienteventinputaudiobuffercommit) event. The commit creates a new user message item in the conversation.
+- The server responds by sending the [`input_audio_buffer.committed`](../realtime-audio-reference.md#realtimeservereventinputaudiobuffercommitted) event.
+- The server responds by sending the [`conversation.item.created`](../realtime-audio-reference.md#realtimeservereventconversationitemcreated) event.
+
+:::image type="content" source="../media/how-to/real-time/input-audio-buffer-client-managed.png" alt-text="Diagram of the Realtime API input audio sequence without server decision mode." lightbox="../media/how-to/real-time/input-audio-buffer-client-managed.png":::
+
+<!--
+sequenceDiagram
+  participant Client as Client
+  participant Server as Server
+  Client->>Server: input_audio_buffer.append
+  Server->>Server: Append audio to buffer
+  Client->>Server: input_audio_buffer.commit
+  Server->>Server: Commit audio buffer
+  Server->>Client: input_audio_buffer.committed
+  Server->>Client: conversation.item.created
+-->
+
+### Server decision mode
+
+The session can be configured with the `turn_detection` type set to `server_vad`. In this case, the server evaluates user audio from the client (as sent via [`input_audio_buffer.append`](../realtime-audio-reference.md#realtimeclienteventinputaudiobufferappend)) using a voice activity detection (VAD) component. The server automatically uses that audio to initiate response generation on applicable conversations when an end of speech is detected. Silence detection for the VAD can be configured when specifying `server_vad` detection mode.
+
+- The server sends the [`input_audio_buffer.speech_started`](../realtime-audio-reference.md#realtimeservereventinputaudiobufferspeechstarted) event when it detects the start of speech.
+- At any time, the client can optionally append audio to the buffer by sending the [`input_audio_buffer.append`](../realtime-audio-reference.md#realtimeclienteventinputaudiobufferappend) event.
+- The server sends the [`input_audio_buffer.speech_stopped`](../realtime-audio-reference.md#realtimeservereventinputaudiobufferspeechstopped) event when it detects the end of speech.
+- The server commits the input audio buffer by sending the [`input_audio_buffer.committed`](../realtime-audio-reference.md#realtimeservereventinputaudiobuffercommitted) event.
+- The server sends the [`conversation.item.created`](../realtime-audio-reference.md#realtimeservereventconversationitemcreated) event with the user message item created from the audio buffer.
+
+:::image type="content" source="../media/how-to/real-time/input-audio-buffer-server-vad.png" alt-text="Diagram of the Realtime API input audio sequence with server decision mode." lightbox="../media/how-to/real-time/input-audio-buffer-server-vad.png":::
+
+
+<!-- 
+sequenceDiagram
+    participant Client as Client
+    participant Server as Server
+    Server->>Client: input_audio_buffer.speech_started
+    Client->>Server: input_audio_buffer.append (optional)
+    Server->>Server: Append audio to buffer
+    Server->>Client: input_audio_buffer.speech_stopped
+    Server->>Server: Commit audio buffer
+    Server->>Client: input_audio_buffer.committed
+    Server->>Client: conversation.item.created
+-->
+
+## Conversation and response generation
+
+You can have one active conversation per session. The conversation accumulates input signals until a response is started, either via a direct event by the caller or automatically by voice activity detection (VAD).
+
+- The server [`conversation.created`](../realtime-audio-reference.md#realtimeservereventconversationcreated) event is returned right after session creation.
+- The client adds new items to the conversation with a [`conversation.item.create`](../realtime-audio-reference.md#realtimeclienteventconversationitemcreate) event.
+- The server [`conversation.item.created`](../realtime-audio-reference.md#realtimeservereventconversationitemcreated) event is returned when the client adds a new item to the conversation.
+
+Optionally, the client can truncate or delete items in the conversation:
+- The client truncates an earlier assistant audio message item with a [`conversation.item.truncate`](../realtime-audio-reference.md#realtimeclienteventconversationitemtruncate) event.
+- The server [`conversation.item.truncated`](../realtime-audio-reference.md#realtimeservereventconversationitemtruncated) event is returned to sync the client and server state.
+- The client deletes an item in the conversation with a [`conversation.item.delete`](../realtime-audio-reference.md#realtimeclienteventconversationitemdelete) event.
+- The server [`conversation.item.deleted`](../realtime-audio-reference.md#realtimeservereventconversationitemdeleted) event is returned to sync the client and server state.
+
+:::image type="content" source="../media/how-to/real-time/conversation-item-sequence.png" alt-text="Diagram of the Realtime API conversation item sequence." lightbox="../media/how-to/real-time/conversation-item-sequence.png":::
+
+<!-- 
+sequenceDiagram
+  participant Client as Client
+  participant Server as Server
+  Server->>Client: conversation.created
+  Client->>Server: conversation.item.create
+  Server->>Server: Create item
+  Server->>Client: conversation.item.created
+  Client->>Server: conversation.item.truncate
+  Server->>Server: Truncate item
+  Server->>Client: conversation.item.truncated
+  Client->>Server: conversation.item.delete
+  Server->>Server: Delete item
+  Server->>Client: conversation.item.deleted
+-->
+
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムAPIの更新と構成"
}
```

### Explanation
今回の変更では、リアルタイムAPIに関するドキュメントの内容が更新され、いくつかのセクションが追加、修正、または整理されました。主な改訂ポイントは、WebSocket接続による認証と機能的相互作用の流れを図示し、イベントの送受信、セッションの構成、音声活動検出（VAD）を利用したデータフローの制御について詳述されていることです。

具体的には、新しい画像やダイアグラムが追加され、ユーザが実際にAPIを使用する際のフローが視覚的に理解しやすくなっています。また、セッション管理や応答生成の重要な側面について、詳しく説明され、例を通じて具体的な使い方が示されています。

さらに、音声入力バッファの管理や新しいアイテムの追加、トランザクションの削除といった機能についても触れています。この更新により、APIの利用者は、リアルタイムでの音声データ処理の理解を深め、よりスムーズに実装を進められることでしょう。

## articles/ai-services/openai/media/how-to/global-batch/create-batch-job.png{#item-fd1371}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチジョブ作成画像の削除"
}
```

### Explanation
この変更では、リポジトリ内の「create-batch-job.png」という画像ファイルが削除されました。この画像は、グローバルバッチジョブの作成方法に関連していたと考えられますが、今後のドキュメントにおいては必要なくなったため、削除された可能性があります。

画像の削除により、関連するコンテンツが更新されたのか、または代替の視覚的資料が提供される予定があるのかもしれません。ユーザーに与える影響は少ないと考えられますが、今後のドキュメントの変更や更新には留意する必要があります。

## articles/ai-services/openai/media/how-to/real-time/conversation-item-sequence.png{#item-4caf37}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話アイテムシーケンス画像の追加"
}
```

### Explanation
この変更では、新しい画像ファイル「conversation-item-sequence.png」が追加されました。この画像は、リアルタイムAPIに関連する会話のアイテムシーケンスを視覚的に示すものと考えられます。

この追加により、ユーザーは会話の流れやアイテムの生成過程をより直感的に理解できるようになります。特にAPIの使用方法を学んでいる開発者にとって、視覚的な資料は重要な理解を促進するため、この変更はドキュメントの価値を高めるものと評価できます。

## articles/ai-services/openai/media/how-to/real-time/input-audio-buffer-client-managed.png{#item-07f39e}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クライアント管理の入力音声バッファ画像の追加"
}
```

### Explanation
この変更では、「input-audio-buffer-client-managed.png」という新しい画像ファイルが追加されました。この画像は、リアルタイム音声処理におけるクライアント管理の入力音声バッファを視覚的に示すものであると考えられます。

この新しいビジュアル素材は、開発者やユーザーが音声データの処理方法を理解するのを助ける役割を果たします。特に、音声認識や音声合成などの機能を利用しようとしているユーザーにとって、具体的な例として画像が提供されることで、実装の理解が深まるでしょう。この追加により、ドキュメント全体の教育効果が高まると期待されます。

## articles/ai-services/openai/media/how-to/real-time/input-audio-buffer-server-vad.png{#item-223de3}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーVADの入力音声バッファ画像の追加"
}
```

### Explanation
この変更では、「input-audio-buffer-server-vad.png」という新しい画像ファイルが追加されました。この画像は、リアルタイム音声処理におけるサーバーベースの音声活動検出（VAD）を用いた入力音声バッファの概念を視覚的に表すものです。

新たに追加されたこのビジュアル素材は、開発者や利用者がサーバーサイドでの音声データ処理の仕組みを理解するのに役立ちます。特に、音声認識技術やVAD技術に関心を持つユーザーにとって、具体的な視覚資料が提供されることで、より深い理解を促進することが期待されます。この改良により、関連するドキュメントの教育的価値が向上するでしょう。

## articles/ai-services/openai/media/how-to/real-time/realtime-api-sequence.png{#item-af9ae0}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムAPIシーケンス画像の追加"
}
```

### Explanation
この変更では、「realtime-api-sequence.png」という新しい画像ファイルが追加されました。この画像は、リアルタイムAPIの処理フローやシーケンスを視覚的に説明するためのものであり、ユーザーがAPIの動作を理解するのを助ける役割を果たします。

追加されたこのビジュアルは、開発者や利用者に対し、リアルタイムでのデータ処理や音声処理に関する具体的な情報を提供します。特に、APIの利用方法やそのフローを明示することで、実装の理解の助けになり、よりスムーズな開発や使用を促進することが期待されます。この新しい素材がドキュメント全体にどのように寄与するかが注目されます。

## articles/ai-services/openai/media/how-to/working-with-models/deployments-new.png{#item-23a410}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのデプロイメント画像の削除"
}
```

### Explanation
この変更では、「deployments-new.png」という画像ファイルが削除されました。この画像は、モデルのデプロイメントに関連する情報を視覚的に提供していたものです。

画像の削除は、ドキュメントの内容が更新された結果である可能性があり、より正確な情報や新しいビジュアルが必要とされる状況を反映しています。削除されたことにより、ユーザーは古い情報に基づいて判断するリスクが減少し、より信頼性の高い資料を利用できるようになります。今後の更新で新たなビジュアルが追加されることが予想され、より最新の情報をもとにしたサポートが提供されることでしょう。

## articles/ai-services/openai/media/monitoring/azure-openai-studio-playground.png{#item-754487}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI スタジオのプレイグラウンド画像の削除"
}
```

### Explanation
この変更では、「azure-openai-studio-playground.png」という画像ファイルが削除されました。この画像は、Azure OpenAI スタジオのプレイグラウンド機能を説明するために使用されていたと考えられます。

画像の削除は、内容が古くなった、または新しいビジュアルが用意される予定であることを示唆しています。これにより、ユーザーはより正確で現在の情報にアクセスできるようになり、最新の機能やインターフェースの理解が容易になります。今後の更新において、新しい画像やより効果的な説明が追加されることが期待されています。

## articles/ai-services/openai/media/provisioned/quota.png{#item-9e5234}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングのクオータ画像の削除"
}
```

### Explanation
この変更では、「quota.png」という画像ファイルが削除されました。この画像は、プロビジョニングに関連するクオータ情報を視覚的に説明するために使用されていたと推測されます。

画像の削除により、ドキュメントの内容が古くなったことを反映している可能性や、より新しい情報を提供するために更新が行われていることが示されます。これにより、ユーザーは最新のガイドラインやデータに基づいて正確な理解を深めることができるようになります。今後の更新において、新たな説明やビジュアルが追加されることが期待されます。

## articles/ai-services/openai/media/quickstarts/dall-e-studio-new.png{#item-136e43}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-E スタジオの新しい画像の削除"
}
```

### Explanation
この変更では、「dall-e-studio-new.png」という画像ファイルが削除されました。この画像は、DALL-E スタジオのクイックスタートガイドやチュートリアルに関連して使用されていたものであると考えられます。

画像の削除は、ドキュメントの更新が行われている可能性を示唆しており、内容が古くなったため新しいビジュアルが用意されることが期待されます。ユーザーは、最新の機能やインターフェースに基づいた正確な情報にアクセスできるようになるため、理解や使用が容易になります。今後、関連する新しいビジュアルや情報が追加されることが期待されます。

## articles/ai-services/openai/media/quickstarts/studio-vision-enhanced-video.png{#item-a59d96}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタジオビジョンの強化動画の画像削除"
}
```

### Explanation
この変更により、「studio-vision-enhanced-video.png」という画像ファイルが削除されました。この画像は、スタジオビジョン機能のクイックスタートガイドに関連して使用されていた可能性があります。

画像の削除は、ドキュメントが更新されていることを示唆しており、情報内容の更新や新しいビジュアルが用意されることが期待されます。これにより、ユーザーは、最新の機能や使用方法に関する正確な情報にアクセスできるようになり、ガイドラインに基づいた理解が促進されます。今後、関連する新しいコンテンツや画像が提供されることが期待されます。

## articles/ai-services/openai/media/quickstarts/studio-vision-enhanced.png{#item-4282af}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタジオビジョンの強化画像の削除"
}
```

### Explanation
この変更では、「studio-vision-enhanced.png」という画像ファイルが削除されました。この画像は、スタジオビジョンに関連したクイックスタートガイドでの使用が想定されていたものです。

この削除は、関連情報の更新や整理の一環として行われることが考えられます。ユーザーに最新の情報を提供し、古くなったコンテンツを排除することで、より明確で正確なガイドラインの提示を目指します。今後、新しい画像やコンテンツが追加される可能性があり、利用者の理解を助けるための改良が期待されます。

## articles/ai-services/openai/media/quickstarts/studio-vision.png{#item-a5dbbb}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタジオビジョン画像の削除"
}
```

### Explanation
この変更によって、「studio-vision.png」という画像ファイルが削除されました。この画像は、スタジオビジョンに関するクイックスタートガイドの一部として利用されていたと考えられます。

画像の削除は、ドキュメントが定期的に見直され、更新されていることを示しています。このプロセスは、ユーザーに最新の情報を提供するために重要であり、古いビジュアルや関連性の薄いコンテンツを排除することに寄与します。今後、適切な新しいコンテンツや画像が追加されることで、ユーザーの理解をさらに深めることが期待されます。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -66,7 +66,7 @@ There are nine client events that can be sent from the client to the server:
 
 ### RealtimeClientEventConversationItemCreate
 
-Add a new item to the conversation's context, including messages, function calls, and function call responses. This event can be used to populate a history of the conversation and to add new items mid-stream. Currently this event can't populate assistant audio messages.
+The client `conversation.item.create` event is used to add a new item to the conversation's context, including messages, function calls, and function call responses. This event can be used to populate a history of the conversation and to add new items mid-stream. Currently this event can't populate assistant audio messages.
 
 If successful, the server responds with a `conversation.item.created` event, otherwise an `error` event is sent.
 
@@ -81,15 +81,17 @@ If successful, the server responds with a `conversation.item.created` event, oth
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.item.create`. | **Required**<br>Allowed values: `conversation.item.create` |
-| previous_item_id | string | The ID of the preceding item after which the new item is inserted. If not set, the new item is appended to the end of the conversation. If set, it allows an item to be inserted mid-conversation. If the ID can't be found, then an error is returned and the item isn't added. |  |
-| item | [RealtimeConversationRequestItem](#realtimeconversationrequestitem) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `conversation.item.create`. | 
+| previous_item_id | string | The ID of the preceding item after which the new item is inserted. If not set, the new item is appended to the end of the conversation. If set, it allows an item to be inserted mid-conversation. If the ID can't be found, then an error is returned and the item isn't added. | 
+| item | [RealtimeConversationRequestItem](#realtimeconversationrequestitem) | The item to add to the conversation. | 
 
 ### RealtimeClientEventConversationItemDelete
 
-Send this client event when you want to remove any item from the conversation history. The server responds with a `conversation.item.deleted` event, unless the item doesn't exist in the conversation history, in which case the server responds with an error.
+The client `conversation.item.delete` event is used to remove an item from the conversation history. 
+
+The server responds with a `conversation.item.deleted` event, unless the item doesn't exist in the conversation history, in which case the server responds with an error.
 
 #### Event structure
 
@@ -102,18 +104,18 @@ Send this client event when you want to remove any item from the conversation hi
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.item.delete`. | **Required**<br>Allowed values: `conversation.item.delete` |
-| item_id | string | The ID of the item to delete. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.delete`. |
+| item_id | string | The ID of the item to delete. | 
 
 ### RealtimeClientEventConversationItemTruncate
 
-Send this client event to truncate a previous assistant message's audio. The server produces audio faster than realtime, so this event is useful when the user interrupts to truncate audio that was sent to the client but not yet played. The server's understanding of the audio with the client's playback is synchronized.
+The client `conversation.item.truncate` event is used to truncate a previous assistant message's audio. The server produces audio faster than realtime, so this event is useful when the user interrupts to truncate audio that was sent to the client but not yet played. The server's understanding of the audio with the client's playback is synchronized.
 
 Truncating audio deletes the server-side text transcript to ensure there isn't text in the context that the user doesn't know about.
 
-If successful, the server responds with a `conversation.item.truncated` event.
+If the client event is successful, the server responds with a `conversation.item.truncated` event.
 
 #### Event structure
 
@@ -128,18 +130,20 @@ If successful, the server responds with a `conversation.item.truncated` event.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.item.truncate`. | **Required**<br>Allowed values: `conversation.item.truncate` |
-| item_id | string | The ID of the assistant message item to truncate. Only assistant message items can be truncated. | **Required** |
-| content_index | integer | The index of the content part to truncate. Set this property to "0". | **Required** |
-| audio_end_ms | integer | Inclusive duration up to which audio is truncated, in milliseconds. If the audio_end_ms is greater than the actual audio duration, the server responds with an error. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.truncate`. | 
+| item_id | string | The ID of the assistant message item to truncate. Only assistant message items can be truncated. | 
+| content_index | integer | The index of the content part to truncate. Set this property to "0". | 
+| audio_end_ms | integer | Inclusive duration up to which audio is truncated, in milliseconds. If the audio_end_ms is greater than the actual audio duration, the server responds with an error. | 
 
 ### RealtimeClientEventInputAudioBufferAppend
 
-Send this client event to append audio bytes to the input audio buffer. The audio buffer is temporary storage you can write to and later commit. In Server VAD (Voice Activity Detection) mode, the audio buffer is used to detect speech and the server decides when to commit. When Server VAD is disabled, you must commit the audio buffer manually.
+The client `input_audio_buffer.append` event is used to append audio bytes to the input audio buffer. The audio buffer is temporary storage you can write to and later commit. 
 
-The client can choose how much audio to place in each event up to a maximum of 15 MiB, for example streaming smaller chunks from the client can allow the VAD to be more responsive. Unlike made other client events, the server doesn't send a confirmation response to this event.
+In Server VAD (Voice Activity Detection) mode, the audio buffer is used to detect speech and the server decides when to commit. When server VAD is disabled, the client can choose how much audio to place in each event up to a maximum of 15 MiB. For example, streaming smaller chunks from the client can allow the VAD to be more responsive. 
+
+Unlike made other client events, the server doesn't send a confirmation response to client `input_audio_buffer.append` event.
 
 #### Event structure
 
@@ -152,14 +156,16 @@ The client can choose how much audio to place in each event up to a maximum of 1
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `input_audio_buffer.append`. | **Required**<br>Allowed values: `input_audio_buffer.append` |
-| audio | string | Base64-encoded audio bytes. This value must be in the format specified by the `input_audio_format` field in the session configuration. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `input_audio_buffer.append`. | 
+| audio | string | Base64-encoded audio bytes. This value must be in the format specified by the `input_audio_format` field in the session configuration. | 
 
 ### RealtimeClientEventInputAudioBufferClear
 
-Send this client event to clear the audio bytes in the buffer. The server responds with an `input_audio_buffer.cleared` event.
+The client `input_audio_buffer.clear` event is used to clear the audio bytes in the buffer. 
+
+The server responds with an `input_audio_buffer.cleared` event.
 
 #### Event structure
 
@@ -171,15 +177,19 @@ Send this client event to clear the audio bytes in the buffer. The server respon
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `input_audio_buffer.clear`. | **Required**<br>Allowed values: `input_audio_buffer.clear` |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `input_audio_buffer.clear`. | 
 
 ### RealtimeClientEventInputAudioBufferCommit
 
-Send this client event to commit the user input audio buffer, which creates a new user message item in the conversation. This event produces an error if the input audio buffer is empty. When in server VAD mode, the client doesn't need to send this event, the server commits the audio buffer automatically.
+The client `input_audio_buffer.commit` event is used to commit the user input audio buffer, which creates a new user message item in the conversation. Audio is transcribed if `input_audio_transcription` is configured for the session.
+ 
+When in server VAD mode, the client doesn't need to send this event, the server commits the audio buffer automatically. Without server VAD, the client must commit the audio buffer to create a user message item. This client event produces an error if the input audio buffer is empty. 
+
+Committing the input audio buffer doesn't create a response from the model. 
 
-Committing the input audio buffer triggers input audio transcription (if enabled in session configuration), but it doesn't create a response from the model. The server responds with an `input_audio_buffer.committed` event.
+The server responds with an `input_audio_buffer.committed` event.
 
 #### Event structure
 
@@ -191,13 +201,15 @@ Committing the input audio buffer triggers input audio transcription (if enabled
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `input_audio_buffer.commit`. | **Required**<br>Allowed values: `input_audio_buffer.commit` |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `input_audio_buffer.commit`. | 
 
 ### RealtimeClientEventResponseCancel
 
-Send this client event to cancel an in-progress response. The server responds with a `response.cancelled` event or an error if there's no response to cancel.
+The client `response.cancel` event is used to cancel an in-progress response. 
+
+The server responds with a `response.cancelled` event or an error if there's no response to cancel.
 
 #### Event structure
 
@@ -209,20 +221,21 @@ Send this client event to cancel an in-progress response. The server responds wi
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.cancel`. | **Required**<br>Allowed values: `response.cancel` |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `response.cancel`. | 
 
 ### RealtimeClientEventResponseCreate
 
-This event instructs the server to create a response, which means triggering model inference. When in server VAD mode, the server creates responses automatically.
+The client `response.create` event is used to instruct the server to create a response via model inferencing. When the session is configured in server VAD mode, the server creates responses automatically.
 
-A response includes at least one item, and can have two, in which case the second is a function call. These items are appended to the conversation history.
+A response includes at least one `item`, and can have two, in which case the second is a function call. These items are appended to the conversation history.
 
-The server responds with a `response.created` event, events for items and content created, and finally a `response.done` event to indicate the response is complete.
+The server responds with a [`response.created`](#realtimeservereventresponsecreated) event, one or more item and content events (such as `conversation.item.created` and `response.content_part.added`), and finally a [`response.done`](#realtimeservereventresponsedone) event to indicate the response is complete.
 
-The `response.create` event includes inference configuration like 
-`instructions`, and `temperature`. These fields override the session's configuration for this response only.
+> [!NOTE]
+> The client `response.create` event includes inference configuration like 
+`instructions`, and `temperature`. These fields can override the session's configuration for this response only.
 
 #### Event structure
 
@@ -234,16 +247,18 @@ The `response.create` event includes inference configuration like
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.create`. | **Required**<br>Allowed values: `response.create` |
-| response | [RealtimeResponseOptions](#realtimeresponseoptions) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `response.create`. | 
+| response | [RealtimeResponseOptions](#realtimeresponseoptions) | The response options. |
 
 ### RealtimeClientEventSessionUpdate
 
-Send this client event to update the session's default configuration. The client can send this event at any time to update the session configuration, and any field can be updated at any time, except for voice. The server responds with a `session.updated` event that shows the full effective configuration. 
+The client `session.update` event is used to update the session's default configuration. The client can send this event at any time to update the session configuration, and any field can be updated at any time, except for voice. 
+
+Only fields that are present are updated. To clear a field (such as `instructions`), pass an empty string. 
 
-Only fields that are present are updated, thus the correct way to clear a field like "instructions" is to pass an empty string.
+The server responds with a `session.updated` event that contains the full effective configuration.
 
 #### Event structure
 
@@ -255,10 +270,10 @@ Only fields that are present are updated, thus the correct way to clear a field
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `session.update`. | **Required**<br>Allowed values: `session.update` |
-| session | [RealtimeRequestSession](#realtimerequestsession) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `session.update`. | 
+| session | [RealtimeRequestSession](#realtimerequestsession) | The session configuration. |
 
 ## Server events
 
@@ -279,25 +294,25 @@ There are 28 server events that can be received from the server:
 | [RealtimeServerEventInputAudioBufferSpeechStopped](#realtimeservereventinputaudiobufferspeechstopped) | Server event in server turn detection mode when speech stops. |
 | [RealtimeServerEventRateLimitsUpdated](#realtimeservereventratelimitsupdated) | Emitted after every "response.done" event to indicate the updated rate limits. |
 | [RealtimeServerEventResponseAudioDelta](#realtimeservereventresponseaudiodelta) | Server event when the model-generated audio is updated. |
-| [RealtimeServerEventResponseAudioDone](#realtimeservereventresponseaudiodone) | Server event when the model-generated audio is done. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseAudioDone](#realtimeservereventresponseaudiodone) | Server event when the model-generated audio is done. Also emitted when a response is interrupted, incomplete, or canceled. |
 | [RealtimeServerEventResponseAudioTranscriptDelta](#realtimeservereventresponseaudiotranscriptdelta) | Server event when the model-generated transcription of audio output is updated. |
-| [RealtimeServerEventResponseAudioTranscriptDone](#realtimeservereventresponseaudiotranscriptdone) | Server event when the model-generated transcription of audio output is done streaming. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseAudioTranscriptDone](#realtimeservereventresponseaudiotranscriptdone) | Server event when the model-generated transcription of audio output is done streaming. Also emitted when a response is interrupted, incomplete, or canceled. |
 | [RealtimeServerEventResponseContentPartAdded](#realtimeservereventresponsecontentpartadded) | Server event when a new content part is added to an assistant message item during response generation. |
-| [RealtimeServerEventResponseContentPartDone](#realtimeservereventresponsecontentpartdone) | Server event when a content part is done streaming in an assistant message item. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseContentPartDone](#realtimeservereventresponsecontentpartdone) | Server event when a content part is done streaming in an assistant message item. Also emitted when a response is interrupted, incomplete, or canceled. |
 | [RealtimeServerEventResponseCreated](#realtimeservereventresponsecreated) | Server event when a new Response is created. The first event of response creation, where the response is in an initial state of "in_progress". |
 | [RealtimeServerEventResponseDone](#realtimeservereventresponsedone) | Server event when a response is done streaming. Always emitted, no matter the final state. |
 | [RealtimeServerEventResponseFunctionCallArgumentsDelta](#realtimeservereventresponsefunctioncallargumentsdelta) | Server event when the model-generated function call arguments are updated. |
-| [RealtimeServerEventResponseFunctionCallArgumentsDone](#realtimeservereventresponsefunctioncallargumentsdone) | Server event when the model-generated function call arguments are done streaming. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseFunctionCallArgumentsDone](#realtimeservereventresponsefunctioncallargumentsdone) | Server event when the model-generated function call arguments are done streaming. Also emitted when a response is interrupted, incomplete, or canceled. |
 | [RealtimeServerEventResponseOutputItemAdded](#realtimeservereventresponseoutputitemadded) | Server event when a new output item is added to a response. |
-| [RealtimeServerEventResponseOutputItemDone](#realtimeservereventresponseoutputitemdone) | Server event when an output item is done streaming. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseOutputItemDone](#realtimeservereventresponseoutputitemdone) | Server event when an output item is done streaming. Also emitted when a response is interrupted, incomplete, or canceled. |
 | [RealtimeServerEventResponseTextDelta](#realtimeservereventresponsetextdelta) | Server event when the model-generated text is updated. |
-| [RealtimeServerEventResponseTextDone](#realtimeservereventresponsetextdone) | Server event when the model-generated text is done. Also emitted when a response is interrupted, incomplete, or cancelled. |
+| [RealtimeServerEventResponseTextDone](#realtimeservereventresponsetextdone) | Server event when the model-generated text is done. Also emitted when a response is interrupted, incomplete, or canceled. |
 | [RealtimeServerEventSessionCreated](#realtimeservereventsessioncreated) | Server event when a session is created. |
 | [RealtimeServerEventSessionUpdated](#realtimeservereventsessionupdated) | Server event when a session is updated. |
 
 ### RealtimeServerEventConversationCreated
 
-Server event when a conversation is created. Emitted right after session creation.
+The server `conversation.created` event is returned right after session creation. One conversation is created per session.
 
 #### Event structure
 
@@ -313,21 +328,21 @@ Server event when a conversation is created. Emitted right after session creatio
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.created`. | **Required**<br>Allowed values: `conversation.created` |
-| conversation | object | The conversation resource. | **Required**<br>See nested properties next.|
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.created`. | 
+| conversation | object | The conversation resource. | 
 
 #### Conversation properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| id | string | The unique ID of the conversation. |  |
-| object | string | The object type must be `realtime.conversation`. |  |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| id | string | The unique ID of the conversation. | 
+| object | string | The object type must be `realtime.conversation`. | 
 
 ### RealtimeServerEventConversationItemCreated
 
-Server event when a conversation item is created. There are several scenarios that produce this event:
+The server `conversation.item.created` event is returned when a conversation item is created. There are several scenarios that produce this event:
   - The server is generating a response, which if successful produces either one or two items, which is of type `message` (role `assistant`) or type `function_call`.
   - The input audio buffer is committed, either by the client or the server (in `server_vad` mode). The server takes the content of the input audio buffer and adds it to a new user message item.
   - The client sent a `conversation.item.create` event to add a new item to the conversation.
@@ -343,15 +358,15 @@ Server event when a conversation item is created. There are several scenarios th
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.item.created`. | **Required**<br>Allowed values: `conversation.item.created` |
-| previous_item_id | string | The ID of the preceding item in the conversation context, allows the client to understand the order of the conversation. | **Required** |
-| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.created`. | 
+| previous_item_id | string | The ID of the preceding item in the conversation context, allows the client to understand the order of the conversation. | 
+| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) | The item that was created. |
 
 ### RealtimeServerEventConversationItemDeleted
 
-Server event when the client deleted an item in the conversation with a `conversation.item.delete` event. This event is used to synchronize the server's understanding of the conversation history with the client's view.
+The server `conversation.item.deleted` event is returned when the client deleted an item in the conversation with a `conversation.item.delete` event. This event is used to synchronize the server's understanding of the conversation history with the client's view.
 
 #### Event structure
 
@@ -364,16 +379,18 @@ Server event when the client deleted an item in the conversation with a `convers
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.item.deleted`. | **Required**<br>Allowed values: `conversation.item.deleted` |
-| item_id | string | The ID of the item that was deleted. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.deleted`. | 
+| item_id | string | The ID of the item that was deleted. | 
 
 ### RealtimeServerEventConversationItemInputAudioTranscriptionCompleted
 
-This server event is the output of audio transcription for user audio written to the user audio buffer. Transcription begins when the input audio buffer is committed by the client or server (in `server_vad` mode). Transcription runs asynchronously with response creation, so this event can come before or after the response events.
+The server `conversation.item.input_audio_transcription.completed` event is the result of audio transcription for speech written to the audio buffer. 
+
+Transcription begins when the input audio buffer is committed by the client or server (in `server_vad` mode). Transcription runs asynchronously with response creation, so this event can come before or after the response events.
 
-Realtime API models accept audio natively, and thus input transcription is a separate process run on a separate Automatic Speech Recognition (ASR) model, currently always `whisper-1`. Thus the transcript can diverge somewhat from the model's interpretation, and should be treated as a rough guide.
+Realtime API models accept audio natively, and thus input transcription is a separate process run on a separate speech recognition model, currently always `whisper-1`. Thus the transcript can diverge somewhat from the model's interpretation, and should be treated as a rough guide.
 
 #### Event structure
 
@@ -388,16 +405,16 @@ Realtime API models accept audio natively, and thus input transcription is a sep
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.item.input_audio_transcription.completed`. | **Required**<br>Allowed values: `conversation.item.input_audio_transcription.completed` |
-| item_id | string | The ID of the user message item containing the audio. | **Required** |
-| content_index | integer | The index of the content part containing the audio. | **Required** |
-| transcript | string | The transcribed text. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.input_audio_transcription.completed`. | 
+| item_id | string | The ID of the user message item containing the audio. | 
+| content_index | integer | The index of the content part containing the audio. | 
+| transcript | string | The transcribed text. | 
 
 ### RealtimeServerEventConversationItemInputAudioTranscriptionFailed
 
-Server event when input audio transcription is configured, and a transcription request for a user message failed. These events are separate from other `error` events so that the client can identify the related item.
+The server `conversation.item.input_audio_transcription.failed` event is returned when input audio transcription is configured, and a transcription request for a user message failed. This event is separate from other `error` events so that the client can identify the related item.
 
 #### Event structure
 
@@ -416,27 +433,27 @@ Server event when input audio transcription is configured, and a transcription r
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.item.input_audio_transcription.failed`. | **Required**<br>Allowed values: `conversation.item.input_audio_transcription.failed` |
-| item_id | string | The ID of the user message item. | **Required** |
-| content_index | integer | The index of the content part containing the audio. | **Required** |
-| error | object | Details of the transcription error. | **Required**<br>See nested properties next.|
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.input_audio_transcription.failed`. | 
+| item_id | string | The ID of the user message item. | 
+| content_index | integer | The index of the content part containing the audio. | 
+| error | object | Details of the transcription error.<br><br>See nested properties in the next table.|
 
 #### Error properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The type of error. |  |
-| code | string | Error code, if any. |  |
-| message | string | A human-readable error message. |  |
-| param | string | Parameter related to the error, if any. |  |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The type of error. | 
+| code | string | Error code, if any. | 
+| message | string | A human-readable error message. | 
+| param | string | Parameter related to the error, if any. | 
 
 ### RealtimeServerEventConversationItemTruncated
 
-Server event when the client truncates an earlier assistant audio message item with a `conversation.item.truncate` event. This event is used to synchronize the server's understanding of the audio with the client's playback.
+The server `conversation.item.truncated` event is returned when the client truncates an earlier assistant audio message item with a `conversation.item.truncate` event. This event is used to synchronize the server's understanding of the audio with the client's playback.
 
-This action truncates the audio and removes the server-side text transcript to ensure there's no text in the context that the user doesn't know about.
+This event truncates the audio and removes the server-side text transcript to ensure there's no text in the context that the user doesn't know about.
 
 #### Event structure
 
@@ -451,16 +468,16 @@ This action truncates the audio and removes the server-side text transcript to e
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `conversation.item.truncated`. | **Required**<br>Allowed values: `conversation.item.truncated` |
-| item_id | string | The ID of the assistant message item that was truncated. | **Required** |
-| content_index | integer | The index of the content part that was truncated. | **Required** |
-| audio_end_ms | integer | The duration up to which the audio was truncated, in milliseconds. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `conversation.item.truncated`. | 
+| item_id | string | The ID of the assistant message item that was truncated. | 
+| content_index | integer | The index of the content part that was truncated. | 
+| audio_end_ms | integer | The duration up to which the audio was truncated, in milliseconds. | 
 
 ### RealtimeServerEventError
 
-Server event when an error occurs, which could be a client problem or a server problem. Most errors are recoverable and the session stays open. 
+The server `error` event is returned when an error occurs, which could be a client problem or a server problem. Most errors are recoverable and the session stays open.
 
 #### Event structure
 
@@ -478,24 +495,24 @@ Server event when an error occurs, which could be a client problem or a server p
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `error`. | **Required**<br>Allowed values: `error` |
-| error | object | Details of the error. | **Required**<br>See nested properties next.|
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `error`. | 
+| error | object | Details of the error.<br><br>See nested properties in the next table.| 
 
 #### Error properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The type of error (for example, "invalid_request_error", "server_error"). |  |
-| code | string | Error code, if any. |  |
-| message | string | A human-readable error message. |  |
-| param | string | Parameter related to the error, if any. |  |
-| event_id | string | The ID of the client event that caused the error, if applicable. |  |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The type of error. For example, "invalid_request_error" and "server_error" are error types. |
+| code | string | Error code, if any. | 
+| message | string | A human-readable error message. | 
+| param | string | Parameter related to the error, if any. | 
+| event_id | string | The ID of the client event that caused the error, if applicable. | 
 
 ### RealtimeServerEventInputAudioBufferCleared
 
-Server event when the client clears the input audio buffer with a `input_audio_buffer.clear` event.
+The server `input_audio_buffer.cleared` event is returned when the client clears the input audio buffer with a `input_audio_buffer.clear` event.
 
 #### Event structure
 
@@ -507,13 +524,13 @@ Server event when the client clears the input audio buffer with a `input_audio_b
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `input_audio_buffer.cleared`. | **Required**<br>Allowed values: `input_audio_buffer.cleared` |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `input_audio_buffer.cleared`. | 
 
 ### RealtimeServerEventInputAudioBufferCommitted
 
-Server event when an input audio buffer is committed, either by the client or automatically in server VAD mode. The `item_id` property is the ID of the user message item created. Thus a `conversation.item.created` event is also sent to the client.
+The server `input_audio_buffer.committed` event is returned when an input audio buffer is committed, either by the client or automatically in server VAD mode. The `item_id` property is the ID of the user message item created. Thus a `conversation.item.created` event is also sent to the client.
 
 #### Event structure
 
@@ -527,17 +544,20 @@ Server event when an input audio buffer is committed, either by the client or au
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `input_audio_buffer.committed`. | **Required**<br>Allowed values: `input_audio_buffer.committed` |
-| previous_item_id | string | The ID of the preceding item after which the new item is inserted. | **Required** |
-| item_id | string | The ID of the user message item created. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `input_audio_buffer.committed`. | 
+| previous_item_id | string | The ID of the preceding item after which the new item is inserted. | 
+| item_id | string | The ID of the user message item created. | 
 
 ### RealtimeServerEventInputAudioBufferSpeechStarted
 
-Server event when in `server_vad` mode to indicate that speech is detected in the audio buffer. This event can happen any time audio is added to the buffer (unless speech is already detected). The client can want to use this event to interrupt audio playback or provide visual feedback to the user. 
+The server `input_audio_buffer.speech_started` event is returned in `server_vad` mode when speech is detected in the audio buffer. This event can happen any time audio is added to the buffer (unless speech is already detected). 
+
+> [!NOTE]
+> The client might want to use this event to interrupt audio playback or provide visual feedback to the user.
 
-The client should expect to receive a `input_audio_buffer.speech_stopped` event when speech stops. The `item_id` property is the ID of the user message item created when speech stops and is also included in the `input_audio_buffer.speech_stopped` event (unless the client manually commits the audio buffer during VAD activation).
+The client should expect to receive a `input_audio_buffer.speech_stopped` event when speech stops. The `item_id` property is the ID of the user message item created when speech stops. The `item_id` is also included in the `input_audio_buffer.speech_stopped` event unless the client manually commits the audio buffer during VAD activation.
 
 #### Event structure
 
@@ -551,17 +571,17 @@ The client should expect to receive a `input_audio_buffer.speech_stopped` event
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `input_audio_buffer.speech_started`. | **Required**<br>Allowed values: `input_audio_buffer.speech_started` |
-| audio_start_ms | integer | Milliseconds from the start of all audio written to the buffer during the session when speech was first detected. This property corresponds to the beginning of audio sent to the model, and thus includes the `prefix_padding_ms` configured in the session. | **Required** |
-| item_id | string | The ID of the user message item created when speech stops. | **Required** | 
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `input_audio_buffer.speech_started`. | 
+| audio_start_ms | integer | Milliseconds from the start of all audio written to the buffer during the session when speech was first detected. This property corresponds to the beginning of audio sent to the model, and thus includes the `prefix_padding_ms` configured in the session. | 
+| item_id | string | The ID of the user message item created when speech stops. | 
 
 ### RealtimeServerEventInputAudioBufferSpeechStopped
 
-Server event in `server_vad` mode when the server detects the end of speech in 
-the audio buffer. The server also sends an `conversation.item.created` 
-event with the user message item created from the audio buffer.
+The server `input_audio_buffer.speech_stopped` event is returned in `server_vad` mode when the server detects the end of speech in the audio buffer. 
+
+The server also sends a `conversation.item.created` event with the user message item created from the audio buffer.
 
 #### Event structure
 
@@ -575,57 +595,44 @@ event with the user message item created from the audio buffer.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `input_audio_buffer.speech_stopped`. | **Required**<br>Allowed values: `input_audio_buffer.speech_stopped` |
-| audio_end_ms | integer | Milliseconds since the session started when speech stopped. This property corresponds to the end of audio sent to the model, and thus includes the `min_silence_duration_ms` configured in the session. | **Required** |
-| item_id | string | The ID of the user message item created. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The event type must be `input_audio_buffer.speech_stopped`. | 
+| audio_end_ms | integer | Milliseconds since the session started when speech stopped. This property corresponds to the end of audio sent to the model, and thus includes the `min_silence_duration_ms` configured in the session. | 
+| item_id | string | The ID of the user message item created. | 
 
 ### RealtimeServerEventRateLimitsUpdated
 
-Server event emitted at the beginning of a response to indicate the updated rate limits. 
-
-When a response is created some tokens are "reserved" for the output tokens, the rate limits shown here reflect that reservation, which is then adjusted accordingly once the response is completed.
-
-#### Event structure
-
-```json
-{
-  "type": "rate_limits.updated"
-}
-```
-
-#### Properties
-
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `rate_limits.updated`. | **Required**<br>Allowed values: `rate_limits.updated` |
-| rate_limits | array | List of rate limit information. | **Required**<br>Array items: [RealtimeServerEventRateLimitsUpdatedRateLimitsItem](#realtimeservereventratelimitsupdatedratelimitsitem) |
+The server `rate_limits.updated` event is emitted at the beginning of a response to indicate the updated rate limits. 
 
-### RealtimeServerEventRateLimitsUpdatedRateLimitsItem
+When a response is created, some tokens are reserved for the output tokens. The rate limits shown here reflect that reservation, which is then adjusted accordingly once the response is completed.
 
 #### Event structure
 
 ```json
 {
-  "name": "<name>",
-  "limit": 0,
-  "remaining": 0
+  "type": "rate_limits.updated",
+  "rate_limits": [
+    {
+      "name": "<name>",
+      "limit": 0,
+      "remaining": 0,
+      "reset_seconds": 0
+    }
+  ]
 }
 ```
 
 #### Properties
 
 | Field | Type | Description | 
-|------|------|-------------| 
-| name | string | The rate limit property name that this item includes information about. | 
-| limit | integer | The maximum configured limit for this rate limit property. | 
-| remaining | integer | The remaining quota available against the configured limit for this rate limit property. | 
-| reset_seconds | number | The remaining time, in seconds, until this rate limit property is reset. | 
+|-------|------|-------------| 
+| type | string | The event type must be `rate_limits.updated`. | 
+| rate_limits | array of [RealtimeServerEventRateLimitsUpdatedRateLimitsItem](#realtimeservereventratelimitsupdatedratelimitsitem) | The list of rate limit information. | 
 
 ### RealtimeServerEventResponseAudioDelta
 
-Returned when the model-generated audio is updated.
+The server `response.audio.delta` event is returned when the model-generated audio is updated.
 
 #### Event structure
 
@@ -642,18 +649,20 @@ Returned when the model-generated audio is updated.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.audio.delta`. | **Required**<br>Allowed values: `response.audio.delta` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| content_index | integer | The index of the content part in the item's content array. | **Required** |
-| delta | string | Base64-encoded audio data delta. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.audio.delta`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the item. | 
+| output_index | integer | The index of the output item in the response. | 
+| content_index | integer | The index of the content part in the item's content array. | 
+| delta | string | Base64-encoded audio data delta. | 
 
 ### RealtimeServerEventResponseAudioDone
 
-Server event when the model-generated audio is done. Also emitted when a response is interrupted, incomplete, or cancelled.
+The server `response.audio.done` event is returned when the model-generated audio is done. 
+
+This event is also returned when a response is interrupted, incomplete, or canceled.
 
 #### Event structure
 
@@ -669,17 +678,17 @@ Server event when the model-generated audio is done. Also emitted when a respons
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.audio.done`. | **Required**<br>Allowed values: `response.audio.done` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| content_index | integer | The index of the content part in the item's content array. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.audio.done`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the item. | 
+| output_index | integer | The index of the output item in the response. | 
+| content_index | integer | The index of the content part in the item's content array. | 
 
 ### RealtimeServerEventResponseAudioTranscriptDelta
 
-Server event when the model-generated transcription of audio output is updated.
+The server `response.audio_transcript.delta` event is returned when the model-generated transcription of audio output is updated.
 
 #### Event structure
 
@@ -696,18 +705,20 @@ Server event when the model-generated transcription of audio output is updated.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.audio_transcript.delta`. | **Required**<br>Allowed values: `response.audio_transcript.delta` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| content_index | integer | The index of the content part in the item's content array. | **Required** |
-| delta | string | The transcript delta. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.audio_transcript.delta`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the item. | 
+| output_index | integer | The index of the output item in the response. | 
+| content_index | integer | The index of the content part in the item's content array. | 
+| delta | string | The transcript delta. | 
 
 ### RealtimeServerEventResponseAudioTranscriptDone
 
-Server event when the model-generated transcription of audio output is done streaming. Also emitted when a response is interrupted, incomplete, or cancelled.
+The server `response.audio_transcript.done` event is returned when the model-generated transcription of audio output is done streaming. 
+
+This event is also returned when a response is interrupted, incomplete, or canceled.
 
 #### Event structure
 
@@ -724,18 +735,18 @@ Server event when the model-generated transcription of audio output is done stre
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.audio_transcript.done`. | **Required**<br>Allowed values: `response.audio_transcript.done` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| content_index | integer | The index of the content part in the item's content array. | **Required** |
-| transcript | string | The final transcript of the audio. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.audio_transcript.done`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the item. | 
+| output_index | integer | The index of the output item in the response. | 
+| content_index | integer | The index of the content part in the item's content array. | 
+| transcript | string | The final transcript of the audio. | 
 
 ### RealtimeServerEventResponseContentPartAdded
 
-Server event when a new content part is added to an assistant message item during response generation.
+The server `response.content_part.added` event is returned when a new content part is added to an assistant message item during response generation.
 
 #### Event structure
 
@@ -751,14 +762,14 @@ Server event when a new content part is added to an assistant message item durin
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.content_part.added`. | **Required**<br>Allowed values: `response.content_part.added` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the item to which the content part was added. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| content_index | integer | The index of the content part in the item's content array. | **Required** |
-| part | [RealtimeContentPart](#realtimecontentpart) | The content part that was added. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.content_part.added`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the item to which the content part was added. | 
+| output_index | integer | The index of the output item in the response. | 
+| content_index | integer | The index of the content part in the item's content array. | 
+| part | [RealtimeContentPart](#realtimecontentpart) | The content part that was added. | 
 
 #### Part properties
 
@@ -768,7 +779,9 @@ Server event when a new content part is added to an assistant message item durin
 
 ### RealtimeServerEventResponseContentPartDone
 
-Server event when a content part is done streaming in an assistant message item. Also emitted when a response is interrupted, incomplete, or cancelled.
+The server `response.content_part.done` event is returned when a content part is done streaming in an assistant message item. 
+
+This event is also returned when a response is interrupted, incomplete, or canceled.
 
 #### Event structure
 
@@ -784,14 +797,14 @@ Server event when a content part is done streaming in an assistant message item.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.content_part.done`. | **Required**<br>Allowed values: `response.content_part.done` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| content_index | integer | The index of the content part in the item's content array. | **Required** |
-| part | [RealtimeContentPart](#realtimecontentpart) | The content part that is done. | **Required** | 
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.content_part.done`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the item. | 
+| output_index | integer | The index of the output item in the response. | 
+| content_index | integer | The index of the content part in the item's content array. | 
+| part | [RealtimeContentPart](#realtimecontentpart) | The content part that is done. |  
 
 #### Part properties
 
@@ -801,7 +814,7 @@ Server event when a content part is done streaming in an assistant message item.
 
 ### RealtimeServerEventResponseCreated
 
-Server event when a new response is created. The first event of response creation,where  the response is in an initial state of `in_progress`.
+The server `response.created` event is returned when a new response is created. This is the first event of response creation, where the response is in an initial state of `in_progress`.
 
 #### Event structure
 
@@ -813,14 +826,14 @@ Server event when a new response is created. The first event of response creatio
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.created`. | **Required**<br>Allowed values: `response.created` |
-| response | [RealtimeResponse](#realtimeresponse) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.created`. | 
+| response | [RealtimeResponse](#realtimeresponse) | The response object. |
 
 ### RealtimeServerEventResponseDone
 
-Server event when a response is done streaming. Always emitted, no matter the final state. The response object included in the `response.done` event includes all output items in the response but omits the raw audio data.
+The server `response.done` event is returned when a response is done streaming. This event is always emitted, no matter the final state. The response object included in the `response.done` event includes all output items in the response, but omits the raw audio data.
 
 #### Event structure
 
@@ -832,14 +845,14 @@ Server event when a response is done streaming. Always emitted, no matter the fi
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.done`. | **Required**<br>Allowed values: `response.done` |
-| response | [RealtimeResponse](#realtimeresponse) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.done`. | 
+| response | [RealtimeResponse](#realtimeresponse) | The response object. |
 
 ### RealtimeServerEventResponseFunctionCallArgumentsDelta
 
-Server event when the model-generated function call arguments are updated.
+The server `response.function_call_arguments.delta` event is returned when the model-generated function call arguments are updated.
 
 #### Event structure
 
@@ -856,20 +869,20 @@ Server event when the model-generated function call arguments are updated.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.function_call_arguments.delta`. | **Required**<br>Allowed values: `response.function_call_arguments.delta` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the function call item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| call_id | string | The ID of the function call. | **Required** |
-| delta | string | The arguments delta as a JSON string. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.function_call_arguments.delta`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the function call item. | 
+| output_index | integer | The index of the output item in the response. | 
+| call_id | string | The ID of the function call. | 
+| delta | string | The arguments delta as a JSON string. | 
 
 ### RealtimeServerEventResponseFunctionCallArgumentsDone
 
-Server event when the model-generated function call arguments are done streaming.
+The server `response.function_call_arguments.done` event is returned when the model-generated function call arguments are done streaming. 
 
-Also emitted when a response is interrupted, incomplete, or cancelled.
+This event is also returned when a response is interrupted, incomplete, or canceled.
 
 #### Event structure
 
@@ -886,18 +899,18 @@ Also emitted when a response is interrupted, incomplete, or cancelled.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.function_call_arguments.done`. | **Required**<br>Allowed values: `response.function_call_arguments.done` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the function call item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| call_id | string | The ID of the function call. | **Required** |
-| arguments | string | The final arguments as a JSON string. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.function_call_arguments.done`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the function call item. | 
+| output_index | integer | The index of the output item in the response. | 
+| call_id | string | The ID of the function call. | 
+| arguments | string | The final arguments as a JSON string. | 
 
 ### RealtimeServerEventResponseOutputItemAdded
 
-Server event when a new item is created during response generation.
+The server `response.output_item.added` event is returned when a new item is created during response generation.
 
 #### Event structure
 
@@ -911,16 +924,18 @@ Server event when a new item is created during response generation.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.output_item.added`. | **Required**<br>Allowed values: `response.output_item.added` |
-| response_id | string | The ID of the response to which the item belongs. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) |  | **Required** | 
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.output_item.added`. | 
+| response_id | string | The ID of the response to which the item belongs. | 
+| output_index | integer | The index of the output item in the response. | 
+| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) | The item that was added. |
 
 ### RealtimeServerEventResponseOutputItemDone
 
-Server event when an item is done streaming. Also emitted when a response is interrupted, incomplete, or cancelled.
+The server `response.output_item.done` event is returned when an item is done streaming. 
+
+This event is also returned when a response is interrupted, incomplete, or canceled.
 
 #### Event structure
 
@@ -934,16 +949,16 @@ Server event when an item is done streaming. Also emitted when a response is int
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.output_item.done`. | **Required**<br>Allowed values: `response.output_item.done` |
-| response_id | string | The ID of the response to which the item belongs. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.output_item.done`. | 
+| response_id | string | The ID of the response to which the item belongs. | 
+| output_index | integer | The index of the output item in the response. | 
+| item | [RealtimeConversationResponseItem](#realtimeconversationresponseitem) | The item that is done streaming. | 
 
 ### RealtimeServerEventResponseTextDelta
 
-Server event event when the text value of a "text" content part is updated.
+The server `response.text.delta` event is returned when the model-generated text is updated. The text corresponds to the `text` content part of an assistant message item.
 
 #### Event structure
 
@@ -960,19 +975,20 @@ Server event event when the text value of a "text" content part is updated.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.text.delta`. | **Required**<br>Allowed values: `response.text.delta` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| content_index | integer | The index of the content part in the item's content array. | **Required** |
-| delta | string | The text delta. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.text.delta`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the item. | 
+| output_index | integer | The index of the output item in the response. | 
+| content_index | integer | The index of the content part in the item's content array. | 
+| delta | string | The text delta. | 
 
 ### RealtimeServerEventResponseTextDone
 
-Server event when the text value of a "text" content part is done streaming. Also
-emitted when a response is interrupted, incomplete, or cancelled.
+The server `response.text.done` event is returned when the model-generated text is done streaming. The text corresponds to the `text` content part of an assistant message item. 
+
+This event is also returned when a response is interrupted, incomplete, or canceled.
 
 #### Event structure
 
@@ -989,20 +1005,18 @@ emitted when a response is interrupted, incomplete, or cancelled.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `response.text.done`. | **Required**<br>Allowed values: `response.text.done` |
-| response_id | string | The ID of the response. | **Required** |
-| item_id | string | The ID of the item. | **Required** |
-| output_index | integer | The index of the output item in the response. | **Required** |
-| content_index | integer | The index of the content part in the item's content array. | **Required** |
-| text | string | The final text content. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `response.text.done`. | 
+| response_id | string | The ID of the response. | 
+| item_id | string | The ID of the item. | 
+| output_index | integer | The index of the output item in the response. | 
+| content_index | integer | The index of the content part in the item's content array. | 
+| text | string | The final text content. | 
 
 ### RealtimeServerEventSessionCreated
 
-Server event when a session is created. Emitted automatically when a new 
-connection is established as the first server event. This event contains 
-the default session configuration.
+The server `session.created` event is the first server event when you establish a new connection to the Realtime API. This event creates and returns a new session with the default session configuration.
 
 #### Event structure
 
@@ -1014,15 +1028,14 @@ the default session configuration.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `session.created`. | **Required**<br>Allowed values: `session.created` |
-| session | [RealtimeResponseSession](#realtimeresponsesession) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `session.created`. | 
+| session | [RealtimeResponseSession](#realtimeresponsesession) | The session object. | 
 
 ### RealtimeServerEventSessionUpdated
 
-Server event when a session is updated with a `session.update` event, unless 
-there's an error.
+The server `session.updated` event is returned when a session is updated by the client. If there's an error, the server sends an `error` event instead.
 
 #### Event structure
 
@@ -1034,10 +1047,10 @@ there's an error.
 
 #### Properties
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string | The event type must be `session.updated`. | **Required**<br>Allowed values: `session.updated` |
-| session | [RealtimeResponseSession](#realtimeresponsesession) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The event type must be `session.updated`. | 
+| session | [RealtimeResponseSession](#realtimeresponsesession) | The session object. |
 
 ## Components
 
@@ -1057,17 +1070,17 @@ there's an error.
 
 ### RealtimeAudioInputTranscriptionSettings
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| model | [RealtimeAudioInputTranscriptionModel](#realtimeaudioinputtranscriptionmodel) |  | Default: `whisper-1` |
+| Field | Type | Description | 
+|-------|------|-------------|
+| model | [RealtimeAudioInputTranscriptionModel](#realtimeaudioinputtranscriptionmodel) | The default `whisper-1` model is currently the only model supported for audio input transcription. | 
 
 
 ### RealtimeClientEvent
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | [RealtimeClientEventType](#realtimeclienteventtype) |  | **Required** |
-| event_id | string |  |  |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | [RealtimeClientEventType](#realtimeclienteventtype) | The type of the client event. |
+| event_id | string | The unique ID of the event. |
 
 ### RealtimeClientEventType
 
@@ -1085,9 +1098,9 @@ there's an error.
 
 ### RealtimeContentPart
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | [RealtimeContentPartType](#realtimecontentparttype) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | [RealtimeContentPartType](#realtimecontentparttype) | The type of the content part. |
 
 ### RealtimeContentPartType
 
@@ -1104,29 +1117,29 @@ The item to add to the conversation.
 
 ### RealtimeConversationRequestItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | [RealtimeItemType](#realtimeitemtype) |  | **Required** |
-| id | string |  |  |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | [RealtimeItemType](#realtimeitemtype) | The type of the item. |
+| id | string | The unique ID of the item. |
 
 ### RealtimeConversationResponseItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| object | string |  | **Required**<br>Allowed values: `realtime.item` |
-| type | [RealtimeItemType](#realtimeitemtype) |  | **Required** |
-| id | string |  | **Required**<br>This property is nullable. |
+| Field | Type | Description | 
+|-------|------|-------------|
+| object | string | The conversation response item.<br><br>Allowed values: `realtime.item` |
+| type | [RealtimeItemType](#realtimeitemtype) | The type of the item. | 
+| id | string | The unique ID of the item.<br><br>This property is nullable. |
 
 ### RealtimeFunctionTool
 
 The definition of a function tool as used by the realtime endpoint.
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `function` |
-| name | string |  | **Required** |
-| description | string |  |  |
-| parameters |  |  |  |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of the tool.<br><br>Allowed values: `function` |
+| name | string | The name of the function. |
+| description | string | The description of the function. |
+| parameters | object | The parameters of the function. |
 
 ### RealtimeItemStatus
 
@@ -1154,178 +1167,179 @@ The definition of a function tool as used by the realtime endpoint.
 
 ### RealtimeRequestAssistantMessageItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| role | string |  | **Required**<br>Allowed values: `assistant` |
-| content | array |  | **Required**<br>Array items: [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) |
+| Field | Type | Description | 
+|-------|------|-------------|
+| role | string | The role of the message.<br><br>Allowed values: `assistant` | 
+| content | array of [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) | The content of the message. |
 
 ### RealtimeRequestAudioContentPart
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `input_audio` |
-| transcript | string |  |  |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of the content part.<br><br>Allowed values: `input_audio` | 
+| transcript | string | The transcript of the audio. |
 
 ### RealtimeRequestFunctionCallItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `function_call` |
-| name | string |  | **Required** |
-| call_id | string |  | **Required** |
-| arguments | string |  | **Required** |
-| status | [RealtimeItemStatus](#realtimeitemstatus) |  |  |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of the item.<br><br>Allowed values: `function_call` | 
+| name | string | The name of the function call item. |
+| call_id | string | The ID of the function call item. |
+| arguments | string | The arguments of the function call item. |
+| status | [RealtimeItemStatus](#realtimeitemstatus) | The status of the item. |
 
 ### RealtimeRequestFunctionCallOutputItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `function_call_output` |
-| call_id | string |  | **Required** |
-| output | string |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of the item.<br><br>Allowed values: `function_call_output` | 
+| call_id | string | The ID of the function call item. |
+| output | string | The output of the function call item. |
 
 ### RealtimeRequestMessageItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `message` |
-| role | [RealtimeMessageRole](#realtimemessagerole) |  | **Required** |
-| status | [RealtimeItemStatus](#realtimeitemstatus) |  |  |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of the item.<br><br>Allowed values: `message` | 
+| role | [RealtimeMessageRole](#realtimemessagerole) | The role of the message. |
+| status | [RealtimeItemStatus](#realtimeitemstatus) | The status of the item. |
 
 ### RealtimeRequestMessageReferenceItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `message` |
-| id | string |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of the item.<br><br>Allowed values: `message` | 
+| id | string | The ID of the message item. |
 
 ### RealtimeRequestSession
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| modalities | array |  |  |
-| instructions | string |  |  |
-| voice | [RealtimeVoice](#realtimevoice) |  |  |
-| input_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) |  |  |
-| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) |  |  |
-| input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) |  | Nullable |
-| turn_detection | [RealtimeTurnDetection](#realtimeturndetection) |  | Nullable |
-| tools | array |  | Array items: [RealtimeTool](#realtimetool) |
-| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) |  |  |
-| temperature | number |  |  |
-| max_response_output_tokens |  |  |  |
+| Field | Type | Description | 
+|-------|------|-------------|
+| modalities | array | The modalities that the session supports.<br><br>Allowed values: `text`, `audio`<br/><br/>For example, `"modalities": ["text", "audio"]` is the default setting that enables both text and audio modalities. To enable only text, set `"modalities": ["text"]`. You can't enable only audio. |
+| instructions | string | The instructions (the system message) to guide the model's text and audio responses.<br><br>Here are some example instructions to help guide content and format of text and audio responses:<br>`"instructions": "be succinct"`<br>`"instructions": "act friendly"`<br>`"instructions": "here are examples of good responses"`<br><br>Here are some example instructions to help guide audio behavior:<br>`"instructions": "talk quickly"`<br>`"instructions": "inject emotion into your voice"`<br>`"instructions": "laugh frequently"`<br><br>While the model might not always follow these instructions, they provide guidance on the desired behavior. |
+| voice | [RealtimeVoice](#realtimevoice) | The voice used for the model response for the session.<br><br>Once the voice is used in the session for the model's audio response, it can't be changed. | 
+| input_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the input audio. | 
+| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the output audio. | 
+| input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) | The settings for audio input transcription.<br><br>This property is nullable. |
+| turn_detection | [RealtimeTurnDetection](#realtimeturndetection) | The turn detection settings for the session.<br><br>This property is nullable. |
+| tools | array of [RealtimeTool](#realtimetool) | The tools available to the model for the session. |
+| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) | The tool choice for the session. |
+| temperature | number | The sampling temperature for the model. The allowed temperature values are limited to [0.6, 1.2]. Defaults to 0.8. |
+| max_response_output_tokens | integer or "inf" | The maximum number of output tokens per assistant response, inclusive of tool calls.<br><br>Specify an integer between 1 and 4096 to limit the output tokens. Otherwise, set the value to "inf" to allow the maximum number of tokens.<br><br>For example, to limit the output tokens to 1000, set `"max_response_output_tokens": 1000`. To allow the maximum number of tokens, set `"max_response_output_tokens": "inf"`.<br><br>Defaults to `"inf"`. |
 
 ### RealtimeRequestSystemMessageItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| role | string |  | **Required**<br>Allowed values: `system` |
-| content | array |  | **Required**<br>Array items: [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| role | string | The role of the message.<br><br>Allowed values: `system` |
+| content | array of [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) | The content of the message. | 
 
 ### RealtimeRequestTextContentPart
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `input_text` |
-| text | string |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The type of the content part.<br><br>Allowed values: `input_text` |
+| text | string | The text content. |
 
 ### RealtimeRequestUserMessageItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| role | string |  | **Required**<br>Allowed values: `user` |
-| content | array |  | **Required**<br>Array items can be: [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) or [RealtimeRequestAudioContentPart](#realtimerequestaudiocontentpart) |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| role | string | The role of the message.<br><br>Allowed values: `user` |
+| content | array of [RealtimeRequestTextContentPart](#realtimerequesttextcontentpart) or [RealtimeRequestAudioContentPart](#realtimerequestaudiocontentpart) | The content of the message. |
 
 ### RealtimeResponse
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| object | string |  | **Required**<br>Allowed values: `realtime.response` |
-| id | string |  | **Required** |
-| status | [RealtimeResponseStatus](#realtimeresponsestatus) |  | **Required**<br>Default: `in_progress` |
-| status_details | [RealtimeResponseStatusDetails](#realtimeresponsestatusdetails) |  | **Required**<br>This property is nullable. |
-| output | array |  | **Required**<br>Array items: [RealtimeConversationResponseItem](#realtimeconversationresponseitem) |
-| usage | object |  | **Required**<br>See nested properties next.|
-| + total_tokens | integer | A property of the `usage` object. | **Required** |
-| + input_tokens | integer | A property of the `usage` object. | **Required** |
-| + output_tokens | integer | A property of the `usage` object. | **Required** |
-| + input_token_details | object | A property of the `usage` object. | **Required**<br>See nested properties next.|
-| + cached_tokens | integer | A property of the `input_token_details` object. | **Required** |
-| + text_tokens | integer | A property of the `input_token_details` object. | **Required** |
-| + audio_tokens | integer | A property of the `input_token_details` object. | **Required** |
-| + output_token_details | object | A property of the `usage` object. | **Required**<br>See nested properties next.|
-| + text_tokens | integer | A property of the `output_token_details` object. | **Required** |
-| + audio_tokens | integer | A property of the `output_token_details` object. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| object | string | The response object.<br><br>Allowed values: `realtime.response` |
+| id | string | The unique ID of the response. |
+| status | [RealtimeResponseStatus](#realtimeresponsestatus) | The status of the response.<br><br>The default status value is `in_progress`. |
+| status_details | [RealtimeResponseStatusDetails](#realtimeresponsestatusdetails) | The details of the response status.<br><br>This property is nullable. |
+| output | array of [RealtimeConversationResponseItem](#realtimeconversationresponseitem) | The output items of the response. |
+| usage | object | Usage statistics for the response. Each Realtime API session maintains a conversation context and appends new items to the conversation. Output from previous turns (text and audio tokens) is input for later turns.<br><br>See nested properties next.|
+| + total_tokens | integer | The total number of tokens in the Response including input and output text and audio tokens.<br><br>A property of the `usage` object. | 
+| + input_tokens | integer | The number of input tokens used in the response, including text and audio tokens.<br><br>A property of the `usage` object. |
+| + output_tokens | integer | The number of output tokens sent in the response, including text and audio tokens.<br><br>A property of the `usage` object. | 
+| + input_token_details | object | Details about the input tokens used in the response.<br><br>A property of the `usage` object.<br>br><br>See nested properties next.|
+| + cached_tokens | integer | The number of cached tokens used in the response.<br><br>A property of the `input_token_details` object. | 
+| + text_tokens | integer | The number of text tokens used in the response.<br><br>A property of the `input_token_details` object. | 
+| + audio_tokens | integer | The number of audio tokens used in the response.<br><br>A property of the `input_token_details` object. | 
+| + output_token_details | object | Details about the output tokens used in the response.<br><br>A property of the `usage` object.<br><br>See nested properties next.|
+| + text_tokens | integer | The number of text tokens used in the response.<br><br>A property of the `output_token_details` object. | 
+| + audio_tokens | integer | The number of audio tokens used in the response.<br><br>A property of the `output_token_details` object. | 
+
 
 ### RealtimeResponseAudioContentPart
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `audio` |
-| transcript | string |  | **Required**<br>This property is nullable. |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The type of the content part.<br><br>Allowed values: `audio` |
+| transcript | string | The transcript of the audio.<br><br>This property is nullable. |
 
 ### RealtimeResponseBase
 
 The response resource.
 
 ### RealtimeResponseFunctionCallItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `function_call` |
-| name | string |  | **Required** |
-| call_id | string |  | **Required** |
-| arguments | string |  | **Required** |
-| status | [RealtimeItemStatus](#realtimeitemstatus) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The type of the item.<br><br>Allowed values: `function_call` |
+| name | string | The name of the function call item. |
+| call_id | string | The ID of the function call item. |
+| arguments | string | The arguments of the function call item. |
+| status | [RealtimeItemStatus](#realtimeitemstatus) | The status of the item. |
 
 ### RealtimeResponseFunctionCallOutputItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `function_call_output` |
-| call_id | string |  | **Required** |
-| output | string |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The type of the item.<br><br>Allowed values: `function_call_output` |
+| call_id | string | The ID of the function call item. |
+| output | string | The output of the function call item. |
 
 ### RealtimeResponseMessageItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `message` |
-| role | [RealtimeMessageRole](#realtimemessagerole) |  | **Required** |
-| content | array |  | **Required**<br>Array items: [RealtimeContentPart](#realtimecontentpart) |
-| status | [RealtimeItemStatus](#realtimeitemstatus) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------| 
+| type | string | The type of the item.<br><br>Allowed values: `message` |
+| role | [RealtimeMessageRole](#realtimemessagerole) | The role of the message. |
+| content | array | The content of the message.<br><br>Array items: [RealtimeResponseTextContentPart](#realtimeresponsetextcontentpart) |
+| status | [RealtimeItemStatus](#realtimeitemstatus) | The status of the item. |
 
 ### RealtimeResponseOptions
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| modalities | array | The modalities for the response. |  |
-| instructions | string | Instructions for the model. |  |
-| voice | [RealtimeVoice](#realtimevoice) | The voice the model uses to respond - one of `alloy`, `echo`, or `shimmer`. |  |
-| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format of output audio. |  |
-| tools | array | Tools (functions) available to the model. | Array items: [RealtimeTool](#realtimetool) |
-| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) | How the model chooses tools. |  |
-| temperature | number | Sampling temperature. |  |
-| max_output_tokens |  | Maximum number of output tokens for a single assistant response, inclusive of tool calls. Provide an integer between 1 and 4096 to limit output tokens, or "inf" for the maximum available tokens for a given model. Defaults to "inf". |  |
+| Field | Type | Description |
+|-------|------|-------------|
+| modalities | array | The modalities that the session supports.<br><br>Allowed values: `text`, `audio`<br/><br/>For example, `"modalities": ["text", "audio"]` is the default setting that enables both text and audio modalities. To enable only text, set `"modalities": ["text"]`. You can't enable only audio. |
+| instructions | string | The instructions (the system message) to guide the model's text and audio responses.<br><br>Here are some example instructions to help guide content and format of text and audio responses:<br>`"instructions": "be succinct"`<br>`"instructions": "act friendly"`<br>`"instructions": "here are examples of good responses"`<br><br>Here are some example instructions to help guide audio behavior:<br>`"instructions": "talk quickly"`<br>`"instructions": "inject emotion into your voice"`<br>`"instructions": "laugh frequently"`<br><br>While the model might not always follow these instructions, they provide guidance on the desired behavior. |
+| voice | [RealtimeVoice](#realtimevoice) | The voice used for the model response for the session.<br><br>Once the voice is used in the session for the model's audio response, it can't be changed. | 
+| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the output audio. | 
+| tools | array of [RealtimeTool](#realtimetool) | The tools available to the model for the session. |
+| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) | The tool choice for the session. |
+| temperature | number | The sampling temperature for the model. The allowed temperature values are limited to [0.6, 1.2]. Defaults to 0.8. |
+| max__output_tokens | integer or "inf" | The maximum number of output tokens per assistant response, inclusive of tool calls.<br><br>Specify an integer between 1 and 4096 to limit the output tokens. Otherwise, set the value to "inf" to allow the maximum number of tokens.<br><br>For example, to limit the output tokens to 1000, set `"max_response_output_tokens": 1000`. To allow the maximum number of tokens, set `"max_response_output_tokens": "inf"`.<br><br>Defaults to `"inf"`. |
 
 ### RealtimeResponseSession
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| object | string |  | **Required**<br>Allowed values: `realtime.session` |
-| id | string |  | **Required** |
-| model | string |  | **Required** |
-| modalities | array |  | **Required** |
-| instructions | string |  | **Required** |
-| voice | [RealtimeVoice](#realtimevoice) |  | **Required** |
-| input_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) |  | **Required** |
-| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) |  | **Required** |
-| input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) |  | **Required**<br>This property is nullable. |
-| turn_detection | [RealtimeTurnDetection](#realtimeturndetection) |  | **Required** |
-| tools | array |  | **Required**<br>Array items: [RealtimeTool](#realtimetool) |
-| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) |  | **Required** |
-| temperature | number |  | **Required** |
-| max_response_output_tokens |  |  | **Required**<br>This property is nullable. |
+| Field | Type | Description | 
+|-------|------|-------------|
+| object | string | The session object.<br><br>Allowed values: `realtime.session` |
+| id | string | The unique ID of the session. | 
+| model | string | The model used for the session. | 
+| modalities | array | The modalities that the session supports.<br><br>Allowed values: `text`, `audio`<br/><br/>For example, `"modalities": ["text", "audio"]` is the default setting that enables both text and audio modalities. To enable only text, set `"modalities": ["text"]`. You can't enable only audio. |
+| instructions | string | The instructions (the system message) to guide the model's text and audio responses.<br><br>Here are some example instructions to help guide content and format of text and audio responses:<br>`"instructions": "be succinct"`<br>`"instructions": "act friendly"`<br>`"instructions": "here are examples of good responses"`<br><br>Here are some example instructions to help guide audio behavior:<br>`"instructions": "talk quickly"`<br>`"instructions": "inject emotion into your voice"`<br>`"instructions": "laugh frequently"`<br><br>While the model might not always follow these instructions, they provide guidance on the desired behavior. |
+| voice | [RealtimeVoice](#realtimevoice) | The voice used for the model response for the session.<br><br>Once the voice is used in the session for the model's audio response, it can't be changed. | 
+| input_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the input audio. | 
+| output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the output audio. | 
+| input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) | The settings for audio input transcription.<br><br>This property is nullable. |
+| turn_detection | [RealtimeTurnDetection](#realtimeturndetection) | The turn detection settings for the session.<br><br>This property is nullable. |
+| tools | array of [RealtimeTool](#realtimetool) | The tools available to the model for the session. |
+| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) | The tool choice for the session. |
+| temperature | number | The sampling temperature for the model. The allowed temperature values are limited to [0.6, 1.2]. Defaults to 0.8. |
+| max_response_output_tokens | integer or "inf" | The maximum number of output tokens per assistant response, inclusive of tool calls.<br><br>Specify an integer between 1 and 4096 to limit the output tokens. Otherwise, set the value to "inf" to allow the maximum number of tokens.<br><br>For example, to limit the output tokens to 1000, set `"max_response_output_tokens": 1000`. To allow the maximum number of tokens, set `"max_response_output_tokens": "inf"`. |
 
 ### RealtimeResponseStatus
 
@@ -1339,32 +1353,32 @@ The response resource.
 
 ### RealtimeResponseStatusDetails
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | [RealtimeResponseStatus](#realtimeresponsestatus) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | [RealtimeResponseStatus](#realtimeresponsestatus) | The status of the response. |
 
 ### RealtimeResponseTextContentPart
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `text` |
-| text | string |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of the content part.<br><br>Allowed values: `text` |
+| text | string | The text content. |
 
 ### RealtimeServerEvent
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | [RealtimeServerEventType](#realtimeservereventtype) |  | **Required** |
-| event_id | string |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | [RealtimeServerEventType](#realtimeservereventtype) | The type of the server event. |
+| event_id | string | The unique ID of the event. |
 
 ### RealtimeServerEventRateLimitsUpdatedRateLimitsItem
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| name | string | The rate limit property name that this item includes information about. | **Required** |
-| limit | integer | The maximum configured limit for this rate limit property. | **Required** |
-| remaining | integer | The remaining quota available against the configured limit for this rate limit property. | **Required** |
-| reset_seconds | number | The remaining time, in seconds, until this rate limit property is reset. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| name | string | The rate limit property name that this item includes information about. | 
+| limit | integer | The maximum configured limit for this rate limit property. | 
+| remaining | integer | The remaining quota available against the configured limit for this rate limit property. | 
+| reset_seconds | number | The remaining time, in seconds, until this rate limit property is reset. | 
 
 ### RealtimeServerEventType
 
@@ -1401,12 +1415,12 @@ The response resource.
 
 ### RealtimeServerVadTurnDetection
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `server_vad` |
-| threshold | number |  | Default: `0.5` |
-| prefix_padding_ms | string |  |  |
-| silence_duration_ms | string |  |  |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of turn detection.<br><br>Allowed values: `server_vad` |
+| threshold | number | The activation threshold for the server VAD turn detection. In noisy environments, you might need to increase the threshold to avoid false positives. In quiet environments, you might need to decrease the threshold to avoid false negatives.<br><br>Defaults to `0.5`. You can set the threshold to a value between `0.0` and `1.0`. |
+| prefix_padding_ms | string | The duration of speech audio (in milliseconds) to include before the start of detected speech.<br><br>Defaults to `300`. |
+| silence_duration_ms | string | The duration of silence (in milliseconds) to detect the end of speech. You want to detect the end of speech as soon as possible, but not too soon to avoid cutting off the last part of the speech.<br><br>The model will respond more quickly if you set this value to a lower number, but it might cut off the last part of the speech. If you set this value to a higher number, the model will wait longer to detect the end of speech, but it might take longer to respond. |
 
 ### RealtimeSessionBase
 
@@ -1416,9 +1430,9 @@ Realtime session object configuration.
 
 The base representation of a realtime tool definition.
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | [RealtimeToolType](#realtimetooltype) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | [RealtimeToolType](#realtimetooltype) | The type of the tool. |
 
 ### RealtimeToolChoice
 
@@ -1428,11 +1442,11 @@ The combined set of available representations for a realtime tool_choice paramet
 
 The representation of a realtime tool_choice selecting a named function tool.
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | string |  | **Required**<br>Allowed values: `function` |
-| function | object |  | **Required**<br>See nested properties next.|
-| + name | string | A property of the `function` object. | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | string | The type of the tool_choice.<br><br>Allowed values: `function` |
+| function | object | The function tool to select.<br><br>See nested properties next.|
+| + name | string | The name of the function tool.<br><br>A property of the `function` object. | 
 
 ### RealtimeToolChoiceLiteral
 
@@ -1448,9 +1462,9 @@ The available set of mode-level, string literal tool_choice options for the real
 
 A base representation for a realtime tool_choice selecting a named tool.
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | [RealtimeToolType](#realtimetooltype) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | [RealtimeToolType](#realtimetooltype) | The type of the tool_choice. |
 
 ### RealtimeToolType
 
@@ -1463,9 +1477,9 @@ Currently, only 'function' tools are supported.
 
 ### RealtimeTurnDetection
 
-| Field | Type | Description | More Info |
-|-------|------|-------------|----------------|
-| type | [RealtimeTurnDetectionType](#realtimeturndetectiontype) |  | **Required** |
+| Field | Type | Description | 
+|-------|------|-------------|
+| type | [RealtimeTurnDetectionType](#realtimeturndetectiontype) | The type of turn detection.<br><br>Allowed values: `server_vad` |
 
 ### RealtimeTurnDetectionType
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオリファレンスの更新"
}
```

### Explanation
この変更では、「realtime-audio-reference.md」という文書が修正され、大幅なコンテンツの追加と古い情報の削除が行われました。具体的には、496行の新しいコンテンツが追加され、482行が削除されています。

主な変更点には、クライアントとサーバー間でやり取りされるイベントの詳細な説明が含まれており、新しいイベントやその構造、プロパティについての説明が追加されています。例えば、リアルタイムの会話に関するイベントや、そのプロパティ、使い方について具体的に説明しています。こうした変更により、ユーザーがリアルタイムオーディオ機能を理解し、適切に利用できるような情報が提供されています。

この更新は、ドキュメントの整合性を高め、ユーザーの理解を促進するための重要なステップとなります。全体として、この変更はリアルタイム音声処理に関する情報を最新かつ詳細に提供することを目的としています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -322,7 +322,7 @@ items:
     - name: Java
       href: /java/api/com.azure.ai.openai?view=azure-java-preview&preserve-view=true
     - name: JavaScript
-      href: /javascript/api/@azure/openai/?view=azure-node-preview&preserve-view=true
+      href: /azure/ai-services/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-secure%2Ccommand&pivots=programming-language-javascript
     - name: .NET 
       href: /dotnet/api/azure.ai.openai?view=azure-dotnet-preview&preserve-view=true
     - name: REST API (fine-tuning)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptリンクの更新"
}
```

### Explanation
この変更では、`toc.yml`ファイル内でJavaScriptに関するリンクが修正されました。具体的には、JavaScriptの項目から、以前のURLが新しいURLに変更されています。

変更前は以下のリンクが使用されていました：
```
/javascript/api/@azure/openai/?view=azure-node-preview&preserve-view=true
```

変更後のリンクは以下のようになっています：
```
/azure/ai-services/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-secure%2Ccommand&pivots=programming-language-javascript
```

この更新により、JavaScriptに関連する情報への参照がより正確で、現在推奨されている情報へと導かれるようになります。これにより、ユーザーは関連するリソースにアクセスしやすくなり、最新の情報を受け取ることができます。この変更は、ユーザー体験の向上を目的としたマイナーな更新と考えられます。


