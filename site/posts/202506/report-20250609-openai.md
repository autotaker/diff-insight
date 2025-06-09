---
date: '2025-06-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0565698...MicrosoftDocs:35b42f4
summary: リアルタイムオーディオ関連のドキュメントが小規模に更新され、記事の改訂、日付の更新、説明の明確化、コードフォーマットの改善、パラメータ型の変更が行われました。これによりAPIの利用に関するガイダンスが改善され、可読性と実用性が向上しました。新機能としては型情報の詳細化やWebRTCとWebSocketの使用推奨が含まれ、ブレイキングチェンジとしてboolean型から新しい型への変更が実施されました。最近の更新により、開発者はリアルタイムオーディオAPIを効果的に利用できるようになり、音質調整や応答性の要求に応じたカスタム設定や最適化が可能になります。全体的に、これらの変更はエンドユーザーの体験の向上やサービスの競争力強化に寄与することを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0565698...MicrosoftDocs:35b42f4){target="_blank"}

# Highlights
リアルタイムオーディオ関連のドキュメントにおける小規模な更新が行われました。それぞれの記事は改訂され、新しい日付の反映、説明の明確化、コードフォーマットの改善、特定のパラメータ型の変更などが含まれています。これに伴い、APIの利用方法に関するガイダンスが改善され、可読性および実用性が向上しました。

## New features
- エンティティの更新に伴う型情報の詳細化。
- WebRTCおよびWebSocketの適切な使用シーンに関する明確な推奨。

## Breaking changes
- パラメータ型の変更により、従来のboolean型から、`RealtimeAudioInputAudioNoiseReductionSettings`およびstringへの変更が実装されました。

## Other updates
- ドキュメントの日付の更新。
- 可読性を向上させるためのコードと説明のフォーマット調整。

# Insights
最近のドキュメント更新は、開発者がリアルタイムオーディオAPIをより効果的に利用できるように設計されており、技術的な使いやすさと導入のしやすさを考慮した修正がなされています。特に、WebRTCとWebSocketの使用に関する改訂は、接続環境や通信要件に応じた適切な技術選択をサポートするため、パフォーマンスと実装効率の最適化を目指しています。

リアルタイムオーディオ関連の設定では、最新のエンティティやパラメータ型が導入され、プログラム的な柔軟性が向上しています。この変更は、特に音質調整や応答性が要求されるアプリケーションの設計において、必要とされる要件を満たすために重要です。開発者はこれを機に、より精緻なカスタム設定や最適化が可能になり、より高品質な音声通信やインタラクションサービスの実現を目指せるようになっています。

これらの更新は、成果物の品質向上のみならず、エンドユーザーの体験を向上させることを目的としているため、開発コミュニティにとって有益です。最新情報に即した技術的選択が可能になり、結果としてサービスの競争力強化に寄与します。ここで提供されている修正と推奨ガイダンスを活用することで、開発者はより速やかに、予測されるニーズに応じた適切なインフラストラクチャを設計・実装できるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [realtime-audio-webrtc.md](#item-ee05e1) | minor update | リアルタイムオーディオWebRTCに関する記事の更新 | modified | 9 | 11 | 20 | 
| [realtime-audio-websockets.md](#item-568961) | minor update | リアルタイムオーディオWebSocketに関する記事の更新 | modified | 3 | 3 | 6 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | リアルタイムオーディオクイックスタートガイドの更新 | modified | 8 | 3 | 11 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムオーディオリファレンスの更新 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/openai/how-to/realtime-audio-webrtc.md{#item-ee05e1}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use the GPT-4o Realtime API for speech and audio via W
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 4/28/2025
+ms.date: 6/7/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions
@@ -44,16 +44,16 @@ Before you can use GPT-4o real-time audio, you need:
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 - An Azure OpenAI resource created in a [supported region](#supported-models). For more information, see [Create a resource and deploy a model with Azure OpenAI](create-resource.md).
-- You need a deployment of the `gpt-4o-realtime-preview` or `gpt-4o-mini-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section. You can deploy the model from the [Azure AI Foundry model catalog](../../../ai-foundry/how-to/model-catalog-overview.md) or from your project in Azure AI Foundry portal. 
+- You need a deployment of the `gpt-4o-realtime-preview` or `gpt-4o-mini-realtime-preview` model in a supported region as described in the [supported models](#supported-models) section in this article. You can deploy the model from the [Azure AI Foundry model catalog](../../../ai-foundry/how-to/model-catalog-overview.md) or from your project in Azure AI Foundry portal. 
 
 ## Connection and authentication
 
 You use different URLs to get an ephemeral API key and connect to the Realtime API via WebRTC. The URLs are constructed as follows:
 
 | URL | Description | 
 |---|---|
-| Sessions URL | The `/realtime/sessions` URL is used to get an ephemeral API key. The sessions URL includes the Azure OpenAI resource URL, deployment name, the `/realtime/sessions` path, and the API version.<br/><br/>You should use API version `2025-04-01-preview` in the URL.<br/><br/>For an example and more information, see the [Sessions URL](#sessions-url) section below.|
-| WebRTC URL | The WebRTC URL is used to establish a WebRTC peer connection with the Realtime API. The WebRTC URL includes the region and the `realtimeapi-preview.ai.azure.com/v1/realtimertc` path.<br/><br/>The supported regions are `eastus2` and `swedencentral`.<br/><br/>For an example and more information, see the [Sessions URL](#webrtc-url) section below.|
+| Sessions URL | The `/realtime/sessions` URL is used to get an ephemeral API key. The sessions URL includes the Azure OpenAI resource URL, deployment name, the `/realtime/sessions` path, and the API version.<br/><br/>You should use API version `2025-04-01-preview` in the URL.<br/><br/>For an example and more information, see the [Sessions URL](#sessions-url) section in this article.|
+| WebRTC URL | The WebRTC URL is used to establish a WebRTC peer connection with the Realtime API. The WebRTC URL includes the region and the `realtimeapi-preview.ai.azure.com/v1/realtimertc` path.<br/><br/>The supported regions are `eastus2` and `swedencentral`.<br/><br/>For an example and more information, see the [Sessions URL](#webrtc-url) section in this article.|
 
 ### Sessions URL
 Here's an example of a well-constructed `realtime/sessions` URL that you use to get an ephemeral API key:
@@ -156,7 +156,7 @@ The sample code is an HTML page that allows you to start a session with the GPT-
     		
             // The deployment name might not be the same as the model name.
             const DEPLOYMENT = "gpt-4o-mini-realtime-preview"
-    		    const VOICE = "verse"
+    		const VOICE = "verse"
     
             async function StartSession() {
                 try {
@@ -170,8 +170,6 @@ The sample code is an HTML page that allows you to start a session with the GPT-
                     const response = await fetch(SESSIONS_URL, {
                         method: "POST",
                         headers: {
-                            // The Authorization header is commented out because
-                            // currently it isn't supported with the sessions API. 
                             //"Authorization": `Bearer ${ACCESS_TOKEN}`,
                             "api-key": API_KEY,
                             "Content-Type": "application/json"
@@ -188,13 +186,13 @@ The sample code is an HTML page that allows you to start a session with the GPT-
     
                     const data = await response.json();
     				
-            				const sessionId = data.id;
-            				const ephemeralKey = data.client_secret?.value; 
-            				console.error("Ephemeral key:", ephemeralKey);
+                    const sessionId = data.id;
+                    const ephemeralKey = data.client_secret?.value; 
+                    console.error("Ephemeral key:", ephemeralKey);
     				
                     // Mask the ephemeral key in the log message.
                     logMessage("Ephemeral Key Received: " + "***");
-    		            logMessage("WebRTC Session Id = " + sessionId );
+    		        logMessage("WebRTC Session Id = " + sessionId );
                     
                     // Set up the WebRTC connection using the ephemeral key.
                     init(ephemeralKey); 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオWebRTCに関する記事の更新"
}
```

### Explanation
この変更では、リアルタイムオーディオWebRTCに関するドキュメントが更新されました。主な変更点には、日付の更新、いくつかの説明文の改良、コードのフォーマットの整頓が含まれています。具体的には、`ms.date`の値が2025年4月28日から2025年6月7日に変更され、APIのセクションやURLサンプルに関する説明がより明確に編集されました。また、JavaScriptコード内のコメントや変数の整形が改善され、全体的な可読性が向上しています。これにより、ユーザーは新しい情報に基づいて、リアルタイムオーディオAPIをより効果的に利用できるようになります。

## articles/ai-services/openai/how-to/realtime-audio-websockets.md{#item-568961}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use the GPT-4o Realtime API for speech and audio via W
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 4/28/2025
+ms.date: 6/7/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions
@@ -18,9 +18,9 @@ recommendations: false
 
 Azure OpenAI GPT-4o Realtime API for speech and audio is part of the GPT-4o model family that supports low-latency, "speech in, speech out" conversational interactions. 
 
-You can use the Realtime API via WebRTC or WebSocket to send audio input to the model and receive audio responses in real time. Follow the instructions in this article to get started with the Realtime API via WebSockets.
+You can use the Realtime API via WebRTC or WebSocket to send audio input to the model and receive audio responses in real time. 
 
-Use the Realtime API via WebSockets in server-to-server scenarios where low latency isn't a requirement.
+Follow the instructions in this article to get started with the Realtime API via WebSockets. Use the Realtime API via WebSockets in server-to-server scenarios where low latency isn't a requirement.
 
 > [!TIP] 
 > In most cases, we recommend using the [Realtime API via WebRTC](./realtime-audio-webrtc.md) for real-time audio streaming in client-side applications such as a web application or mobile app. WebRTC is designed for low-latency, real-time audio streaming and is the best choice for most use cases.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオWebSocketに関する記事の更新"
}
```

### Explanation
この変更は、リアルタイムオーディオWebSocketに関するドキュメントの軽微な更新を示しています。主な変更点は、日付の更新といくつかの文章の再構成です。具体的には、`ms.date`が2025年4月28日から2025年6月7日に変更され、WebSocketを通じてリアルタイムAPIを利用する際の手順が強調されています。

以前の文から、WebSocketの使用方法に関する詳細な指示が分離され、読みやすく明確になりました。特に、システム間での通信において遅延が必ずしも重要でない場合にWebSocketを使用する場面についての説明が改善され、WebRTCを使用する場合の推奨も明示されています。これにより、ユーザーはWebSocketsを介してリアルタイムAPIを効果的に利用するためのより良いガイダンスを得ることができます。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use GPT-4o Realtime API for speech and audio with Azur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 5/23/2025
+ms.date: 6/7/2025
 author: eric-urban
 ms.author: eur
 ms.custom: references_regions, ignite-2024
@@ -17,9 +17,14 @@ recommendations: false
 
 [!INCLUDE [Feature preview](includes/preview-feature.md)]
 
-Azure OpenAI GPT-4o Realtime API for speech and audio is part of the GPT-4o model family that supports low-latency, "speech in, speech out" conversational interactions. The GPT-4o audio `realtime` API is designed to handle real-time, low-latency conversational interactions, making it a great fit for use cases involving live interactions between a user and a model, such as customer support agents, voice assistants, and real-time translators.
+Azure OpenAI GPT-4o Realtime API for speech and audio is part of the GPT-4o model family that supports low-latency, "speech in, speech out" conversational interactions. 
 
-Most users of the Realtime API need to deliver and receive audio from an end-user in real time, including applications that use WebRTC or a telephony system. The Realtime API isn't designed to connect directly to end user devices and relies on client integrations to terminate end user audio streams. 
+You can use the Realtime API via WebRTC or WebSocket to send audio input to the model and receive audio responses in real time. 
+
+Follow the instructions in this article to get started with the Realtime API via WebSockets. Use the Realtime API via WebSockets in server-to-server scenarios where low latency isn't a requirement.
+
+> [!TIP] 
+> In most cases, we recommend using the [Realtime API via WebRTC](./how-to/realtime-audio-webrtc.md) for real-time audio streaming in client-side applications such as a web application or mobile app. WebRTC is designed for low-latency, real-time audio streaming and is the best choice for most use cases.
 
 ## Supported models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオクイックスタートガイドの更新"
}
```

### Explanation
この変更は、リアルタイムオーディオのクイックスタートガイドに関する軽微な更新を示しています。主な変更点には、日付の更新、文章の整理、WebSocketを介したAPIの使用に関する具体的な指示が含まれます。具体的には、`ms.date`が2025年5月23日から2025年6月7日に変更されました。

新たに、リアルタイムAPIがWebRTCまたはWebSocketを介してオーディオを送受信する方法が強調され、WebSocketについての利用シーンとして、低遅延が要求されないサーバー間の通信が説明されています。また、WebRTCを介した音声ストリーミングが推奨されるケースについても言及されています。この改訂は、ユーザーにリアルタイムAPIを効果的に活用するための明確な手順と推奨を提供します。全体として、ドキュメントはより理解しやすく、実用的な内容に進化しています。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -1390,7 +1390,7 @@ You use the `RealtimeRequestSession` object when you want to update the session
 | voice | [RealtimeVoice](#realtimevoice) | The voice used for the model response for the session.<br><br>Once the voice is used in the session for the model's audio response, it can't be changed. | 
 | input_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the input audio. | 
 | output_audio_format | [RealtimeAudioFormat](#realtimeaudioformat) | The format for the output audio. |
-| input_audio_noise_reduction | boolean | Configuration for input audio noise reduction. This can be set to null to turn off. Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model. Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.<br><br>This property is nullable.| 
+| input_audio_noise_reduction | [RealtimeAudioInputAudioNoiseReductionSettings](#realtimeaudioinputaudionoisereductionsettings) | Configuration for input audio noise reduction. This can be set to null to turn off. Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model. Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.<br><br>This property is nullable.| 
 | input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) | The configuration for input audio transcription. The configuration is null (off) by default. Input audio transcription isn't native to the model, since the model consumes audio directly. Transcription runs asynchronously through the `/audio/transcriptions` endpoint and should be treated as guidance of input audio content rather than precisely what the model heard. For additional guidance to the transcription service, the client can optionally set the language and prompt for transcription.<br><br>This property is nullable. |
 | turn_detection | [RealtimeTurnDetection](#realtimeturndetection) | The turn detection settings for the session.<br><br>This property is nullable. |
 | tools | array of [RealtimeTool](#realtimetool) | The tools available to the model for the session. |
@@ -1662,7 +1662,7 @@ Currently, only 'function' tools are supported.
 | silence_duration_ms | string | The duration of silence (in milliseconds) to detect the end of speech. You want to detect the end of speech as soon as possible, but not too soon to avoid cutting off the last part of the speech.<br><br>The model will respond more quickly if you set this value to a lower number, but it might cut off the last part of the speech. If you set this value to a higher number, the model will wait longer to detect the end of speech, but it might take longer to respond.<br><br>Defaults to `500` milliseconds.<br/><br>This property is only applicable for `server_vad` turn detection. |
 | create_response | boolean | Indicates whether the server will automatically create a response when VAD is enabled and speech stops.<br><br>Defaults to `true`. |
 | interrupt_response | boolean | Indicates whether the server will automatically interrupt any ongoing response with output to the default (`auto`) conversation when a VAD start event occurs.<br><br>Defaults to `true`. |
-| eagerness | boolean | The eagerness of the model to respond and interrupt the user. Specify `low` to wait longer for the user to continue speaking. Specify `high` to chunk the audio as soon as possible for quicker responses. The default value is `auto` that's equivalent to medium.<br/><br>This property is only applicable for `server_vad` turn detection. |
+| eagerness | string | The eagerness of the model to respond and interrupt the user. Specify `low` to wait longer for the user to continue speaking. Specify `high` to chunk the audio as soon as possible for quicker responses. The default value is `auto` that's equivalent to medium.<br/><br>This property is only applicable for `server_vad` turn detection. |
 
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
この変更は、リアルタイムオーディオのリファレンスドキュメントに対する軽微な更新を示しています。変更内容には、いくつかのパラメータに関する説明の修正が含まれています。具体的には、`input_audio_noise_reduction`と`eagerness`のデータ型がそれぞれbooleanから新しい型（`RealtimeAudioInputAudioNoiseReductionSettings`およびstring）に変更されました。

この修正により、これらのプロパティの使用方法や設定が明確になり、開発者がこれらの機能を適切に使用できるように情報が整理されています。他の幾つかのプロパティの説明もコンテキストに合わせて更新されており、ドキュメント全体の一貫性と有用性が向上しています。全体として、この改訂はユーザーにとっての理解を助け、より実用的な情報を提供することを目的としています。


