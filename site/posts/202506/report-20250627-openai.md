---
date: '2025-06-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a20162d...MicrosoftDocs:44ebca9
summary: 今回の更新では、Azure GovernmentおよびAzure OpenAIのドキュメントに対して、リンクの修正や地域リストの追加、目次の更新などの軽微な修正が行われました。特に、Azure
  GovernmentにおけるOpenAIの展開モデルやデータゾーンについての情報が整理され、ファインチューニングモデルの利用可能地域に「南中央アメリカ」と「西ヨーロッパ」が追加されました。破壊的な変更はなく、全体的にドキュメントの明確性とユーザビリティ向上に寄与する内容となっています。これにより、ユーザーはAzure
  Government上でのOpenAI活用法をより明確に理解できるようになり、リアルタイムオーディオ関連のガイドも強化されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a20162d...MicrosoftDocs:44ebca9){target="_blank"}

# ハイライト
Azure GovernmentやAzure OpenAIのドキュメントに対する軽微な更新と修正を中心に、リンクの修正や地域リストの追加、目次の更新といった内容が含まれています。

## 新機能
- Azure GovernmentにおけるOpenAIの展開モデルとデータゾーンの詳細についてのドキュメントが整理されました。
- ファインチューニングモデルの利用可能な地域に「南中央アメリカ（South Central US）」と「西ヨーロッパ（West Europe）」が追加されました。

## 破壊的変更
- 破壊的な変更はこの更新には含まれていません。

## その他の更新
- 「Embeddings models」のリンクテキストが「Embeddings」に変更され、簡潔な表現になりました。
- リアルタイムオーディオに関するドキュメントの名前と内容が具体的なものに変更され、目次もそれに伴い更新されました。

# インサイト
今回の変更は、主にAzure関連のドキュメントの明確性とユーザビリティを向上させることに焦点が当てられています。特に、ドキュメントにおける用語の簡潔化と見出しの調整、利用可能なサービスに関する情報の詳細化が注目されます。

Azure GovernmentにおけるOpenAIの更新では、新たにデータゾーンとモデル展開の詳細が加えられ、ユーザーがどのようにAzure Governmentのインフラ上でOpenAIを活用できるかを明確にしています。これにより、ユーザーは適切なデータセンターを選択しやすくなるでしょう。

ファインチューニングモデルの地域拡大は、Azure OpenAIユーザーが多様な地域でサービスを利用できるようにするためのものであり、地域に縛られないサービス利用の促進が期待されます。

また、リアルタイムオーディオに関するドキュメントの更新では、タイトルの明確化や関連情報の強調によって、APIやイベントを効果的に利用するためのガイドが強化されました。これにより、ユーザーがドキュメントを参考にしながら実装を進めやすくなるでしょう。

全体的に、これらの更新は、ドキュメントの見やすさや使いやすさの向上を意図しており、最終的にはAzure OpenAIのサービス利用の幅を広げることを目指しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure GovernmentにおけるOpenAIの更新 | modified | 18 | 13 | 31 | 
| [models.md](#item-db2c37) | minor update | モデルセクションのリンク修正 | modified | 1 | 1 | 2 | 
| [fine-tune-models.md](#item-2aadea) | minor update | ファインチューニングモデルの更新 | modified | 2 | 0 | 2 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムオーディオ参照の更新 | modified | 9 | 10 | 19 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI in Azure Government
 titleSuffix: Azure OpenAI
 description: Learn how to use Azure OpenAI in the Azure Government cloud.
 author: challenp
-ms.date: 5/29/2025
+ms.date: 6/25/2025
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom:
@@ -25,17 +25,21 @@ The following sections show model availability by region and deployment type. Mo
 
 <br>
 
-## Standard deployment model availability
-|   **Region**  | **o3-mini USGov DataZone** | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-35-turbo**, **0125** | **text-embedding-3-large**, **1** | **text-embedding-3-small**, **1** | **text-embedding-ada-002**, **2** |
-|:--------------|:--------------------------:|:--------------------------:|:-------------------------------:|:--------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
-| usgovarizona  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
-| usgovvirginia | ✅ | ✅ | -  | ✅ | - | - | ✅ |
+### USGov DataZone
+Data zone deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure Government infrastructure to dynamically route traffic to the data center within the USGov data zone with the best availability for each request.
 
 * USGov DataZone provides access to the model from both usgovarizona and usgovvirginia.
 * Data stored at rest remains in the designated Azure region of the resource.
-* Data may be processed for inferencing in either of the two Azure Government regions. 
+* Data may be processed for inferencing in either of the two Azure Government regions.
 
-Data zone standard deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure Government infrastructure to dynamically route traffic to the data center within the USGov data zone with the best availability for each request.
+<br>
+
+### Standard deployment model availability
+|   **Region**   | **o3-mini** | **gpt-4o**, **2024-11-20** | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-35-turbo**, **0125** | **text-embedding-3-large**, **1** | **text-embedding-3-small**, **1** | **text-embedding-ada-002**, **2** |
+|:---------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:--------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
+| usgovarizona   | - | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
+| usgovvirginia  | - | ✅ | ✅ | -  | ✅ | - | - | ✅ |
+| USGov DataZone |✅| ✅ | - | -  | - | - | - | - |
 
 To request quota increases for these models, submit a request at [https://aka.ms/AOAIGovQuota](https://aka.ms/AOAIGovQuota). Note the following maximum quota limits allowed via that form:
 
@@ -45,11 +49,12 @@ To request quota increases for these models, submit a request at [https://aka.ms
 
 <br>
 
-## Provisioned deployment model availability
-|   **Region**  | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-35-turbo**, **0125** |
-|:--------------|:--------------------------:|:-------------------------------:|:--------------------------:|
-| usgovarizona  | ✅ | - | ✅ |
-| usgovvirginia | ✅ | - | ✅ |
+### Provisioned deployment model availability
+|   **Region**  | **gpt-4o**, **2024-11-20** | **gpt-4o**, **2024-05-13** | **gpt-4o-mini**, **2024-07-18** | **gpt-35-turbo**, **0125** |
+|:---------------|:--------------------------:|:--------------------------:|:-------------------------------:|:--------------------------:|
+| usgovarizona   | - | ✅ | - | ✅ |
+| usgovvirginia  | ✅ | ✅ | - | ✅ |
+| USGov DataZone | ✅| -  | -  | -  |
 
 <br>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure GovernmentにおけるOpenAIの更新"
}
```

### Explanation
この変更は、Azure GovernmentにおけるOpenAIのサービスに関連するドキュメントが更新されたことを示しています。具体的には、文書内の展開モデルの可用性と日付が一部修正され、内容が整理されています。

主な変更点には、以下が含まれます：

- 文書の公開日が2025年5月29日から2025年6月25日に更新されました。
- 「USGov DataZone」と「標準展開モデルの可用性」というセクション見出しが追加され、データゾーン展開の詳細な説明やそれに伴うモデルの可用性が整理されています。これにより、ユーザーは、Azure Governmentインフラを使用して、最適なデータセンターに動的にトラフィックをルーティングできることを理解しやすくなります。
- 表の構造が変更され、新しいモデルや地域に関する情報が整理され、より直感的に理解できるように再構築されています。

これらの変更により、ユーザーはAzure GovernmentにおけるOpenAIサービスの使用がより簡単に理解できるようになります。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ Azure OpenAI is powered by a diverse set of models with different capabilities a
 | [GPT-4o & GPT-4o mini & GPT-4 Turbo](#gpt-4o-and-gpt-4-turbo) | The latest most capable Azure OpenAI models with multimodal versions, which can accept both text and images as input. |
 | [GPT-4](#gpt-4) | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
 | [GPT-3.5](#gpt-35) | A set of models that improve on GPT-3 and can understand and generate natural language and code. |
-| [Embeddings](#embeddings-models) | A set of models that can convert text into numerical vector form to facilitate text similarity. |
+| [Embeddings](#embeddings) | A set of models that can convert text into numerical vector form to facilitate text similarity. |
 | [Image generation](#image-generation-models) | A series of models that can generate original images from natural language. |
 | [Audio](#audio-models) | A series of models for speech to text, translation, and text to speech. GPT-4o audio models support either low-latency, "speech in, speech out" conversational interactions or audio generation. |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルセクションのリンク修正"
}
```

### Explanation
この変更は、Azure OpenAIに関するドキュメント内の「モデル」セクションのリンクに関する小規模な修正を示しています。具体的には、"Embeddings"という見出しが "Embeddings models" から "Embeddings" に変更されました。これに伴い、該当するリンクのテキストも簡潔な表現へと修正されています。

この更新によって、リンクの表示名がより正確でシンプルになり、ユーザーが各モデルにアクセスしやすくなることを意図しています。この変更は、ドキュメントの可読性を向上させることに寄与しています。全体として、実質的な機能には影響しない軽微な更新です。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -45,10 +45,12 @@ ms.custom:
 >- Poland Central
 >- Southeast Asia
 >- South Africa North
+>- South Central US
 >- Spain Central
 >- Sweden Central
 >- Switzerland West
 >- Switzerland North
 >- UK South
+>- West Europe
 >- West US
 >- West US3
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングモデルの更新"
}
```

### Explanation
この変更は、ファインチューニングモデルに関するドキュメントの一部を更新したことを示しています。具体的には、サポートされている地域のリストに新しい地域が追加されました。

変更内容は以下の通りです：

- 新たに「南中央アメリカ（South Central US）」と「西ヨーロッパ（West Europe）」が地域リストに追加されました。
- これにより、ファインチューニングモデルが利用可能な地域が拡大し、ユーザーにとっての選択肢が増えることを目的としています。

この更新は、ユーザーが利用できる地域を明確にし、Azure OpenAIのサービスをよりよく理解できるようにするための小規模な修正です。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -1,26 +1,25 @@
 ---
-title: Azure OpenAI in Azure AI Foundry Models Realtime API Reference
+title: Audio events reference
 titleSuffix: Azure OpenAI
-description: Learn how to use the Realtime API to interact with the Azure OpenAI in real-time.
+description: Learn how to use events with the Realtime API and Voice Live API.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 4/28/2025
+ms.date: 6/27/2025
 author: eric-urban
 ms.author: eur
 recommendations: false
 ---
 
-# Realtime events reference
+# Audio events reference
 
-[!INCLUDE [Feature preview](includes/preview-feature.md)]
+Realtime events are used to communicate between the client and server in real-time audio applications. The events are sent as JSON objects over various endpoints, such as WebSockets or WebRTC. The events are used to manage the conversation, audio buffers, and responses in real-time.
 
-The Realtime API is a WebSocket-based API that allows you to interact with the Azure OpenAI in real-time. 
+You can use audio client and server events with these APIs:
+- [Azure OpenAI Realtime API](/azure/ai-services/openai/realtime-audio-quickstart)
+- [Azure AI Voice Live API](/azure/ai-services/speech-service/voice-live)
 
-The Realtime API (via `/realtime`) is built on [the WebSockets API](https://developer.mozilla.org/docs/Web/API/WebSockets_API) to facilitate fully asynchronous streaming communication between the end user and model. Device details like capturing and rendering audio data are outside the scope of the Realtime API. It should be used in the context of a trusted, intermediate service that manages both connections to end users and model endpoint connections. Don't use it directly from untrusted end user devices.
-
-> [!TIP]
-> To get started with the Realtime API, see the [quickstart](realtime-audio-quickstart.md) and [how-to guide](./how-to/realtime-audio.md).
+Unless otherwise specified, the events described in this document are applicable to both APIs.
 
 ## Client events
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオ参照の更新"
}
```

### Explanation
この変更は、Azure OpenAIにおけるリアルタイムオーディオに関するドキュメントのタイトルや説明を更新したことを示しています。主な変更点は以下の通りです：

- ドキュメントのタイトルが「Azure OpenAI in Azure AI Foundry Models Realtime API Reference」から「Audio events reference」に変更され、より具体的な内容を反映しています。
- 説明文も更新され、リアルタイムAPIの使用に加えて、音声ライブAPIとイベント管理に関する情報が含まれるようになりました。
- 一部文が追加され、リアルタイムオーディオアプリケーションにおけるイベントの利用方法が説明されています。

更新後のドキュメントでは、リアルタイムAPIと音声ライブAPIの関連情報が強調されており、ユーザーがこれらのAPIのイベントを効果的に使用するための情報が提供されています。また、APIに関連する具体的な機能や利用方法についても言及されています。全体として、この変更はドキュメントの明確性と使いやすさを向上させることを目的としています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -441,7 +441,7 @@ items:
               displayName: RAG, rag
     - name: Azure OpenAI monitoring data reference
       href: monitor-openai-reference.md
-    - name: Realtime API (preview) events reference
+    - name: Audio events reference
       href: realtime-audio-reference.md
 - name: Resources
   items: 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新"
}
```

### Explanation
この変更は、Azure OpenAIのドキュメントの目次（toc.yml）において、特定の項目の名前を変更したことを示しています。具体的には、以下の変更が行われました：

- 「Realtime API (preview) events reference」という項目名が「Audio events reference」に変更されました。
- これに伴い、リンク先の文書名はそのまま「realtime-audio-reference.md」として保持されています。

この更新により、目次がより明確に内容を反映するようになり、ユーザーがリアルタイムAPIのオーディオイベントに関連する情報を素早く見つけられるようになります。全体として、この変更はユーザーエクスペリエンスを向上させる目的を持っています。


