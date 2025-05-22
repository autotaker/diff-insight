---
date: '2025-05-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f021165...MicrosoftDocs:aedda49
summary: このコードの変更では、Azure OpenAIサービスに関連するドキュメントが更新されています。主な変更点には、リアルタイムオーディオWebSocketのAPIのバージョン更新、強化ファインチューニングのプレビュー表示の明示、o4-miniモデルに関する詳細情報の追加、ユーザーガイドへのリンクの追加が含まれます。破壊的変更はなく、これによりユーザーの利便性が向上しています。特に、最新のAPIバージョンに更新されたことで技術的な互換性が保たれ、新機能への適応が促進されます。また、強化ファインチューニングのステータス明示が現在の機能理解を助け、o4-miniモデルの情報提供がモデル選択を支援しています。最後に、言語や音声オプションに関するリンク追加により、多言語アプリ開発者にとっての利便性が向上しました。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f021165...MicrosoftDocs:aedda49){target="_blank"}

# ハイライト
このコードの変更では、Azure OpenAIサービスに関連する複数のドキュメントが更新されています。主な変更点としては、リアルタイムオーディオWebSocketのAPIバージョン更新、強化ファインチューニングのプレビュー版明示、o4-miniモデルの追加情報、およびユーザーガイドのリンク追加が含まれます。

## 新機能
- o4-miniモデルに関する詳細情報の追加（リリース日、利用可能リージョン、入出力トークン数、トレーニング例のコンテキスト長など）。
  
## 破壊的変更
- 特に破壊的変更は見られません。

## その他の更新
- リアルタイムオーディオWebSocketのAPIバージョンが `2025-04-01-preview` に更新。
- 強化ファインチューニングのドキュメントにプレビュー版であることを示す「(Preview)」表記を追加。
- 強化ファインチューニングに関するリンクが追加され、詳細なガイドへのアクセスが容易に。
- 音声サービスの言語および音声サポートに関するリンクが追加され、利用可能な言語や声がより明確に。

# 洞察
このドキュメント変更は、Azure OpenAIサービスを利用するユーザーにとって必要な情報を更新し、利便性を高めるものである。まず、リアルタイムオーディオを扱うWebSocketに関してAPIバージョンが最新のものに置き換えられたことによって、技術的な互換性の問題を未然に防ぎ、新機能への適応を促している。

また、強化ファインチューニングについて「(Preview)」のステータスを明示することで、ユーザーは現在の機能の提供状況を正しく理解し、試行段階であることを把握することができ、将来的な利用準備や改善要望に対する期待値を調節できる。

さらに、新たにo4-miniモデルに関する情報を追加し、開発者がモデル選択する際の指針を充実させている。具体的なモデル仕様が示されることで、パフォーマンス要件や地域的な制約を踏まえた最適なモデル選択を支援する。

最後に、利用可能な言語や音声オプションに関する情報を容易に確認できるリンクの追加は、マルチリンガルなアプリケーション開発を念頭においた開発者にとって有用である。これにより、より直感的にシステムの調整が行えるようになり、ユーザーエクスペリエンスを向上させることができる。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [realtime-audio-websockets.md](#item-568961) | minor update | リアルタイムオーディオWebSocketのAPIバージョンを更新 | modified | 1 | 1 | 2 | 
| [reinforcement-fine-tuning.md](#item-e8028c) | minor update | 強化ファインチューニングのプレビュー版を明示 | modified | 3 | 3 | 6 | 
| [fine-tune-models.md](#item-2aadea) | minor update | o4-miniモデルの情報を追加 | modified | 1 | 0 | 1 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | 強化ファインチューニングのリンクを追加 | modified | 1 | 1 | 2 | 
| [realtime-audio-quickstart.md](#item-727df8) | minor update | 音声サービスの言語および音声サポートに関するリンクを追加 | modified | 1 | 0 | 1 | 


# Modified Contents
## articles/ai-services/openai/how-to/realtime-audio-websockets.md{#item-568961}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ You can construct a full request URI by concatenating:
 The following example is a well-constructed `/realtime` request URI:
 
 ```http
-wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2024-12-17&deployment=gpt-4o-mini-realtime-preview-deployment-name
+wss://my-eastus2-openai-resource.openai.azure.com/openai/realtime?api-version=2025-04-01-preview&deployment=gpt-4o-mini-realtime-preview-deployment-name
 ```
 
 To authenticate:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオWebSocketのAPIバージョンを更新"
}
```

### Explanation
この変更では、ドキュメントの中のリアルタイムオーディオWebSocketに関するAPIリクエストURIが更新されました。具体的には、APIバージョンが `2024-12-17` から `2025-04-01-preview` に変更されました。この変更は、APIの新しいバージョンに対応するためのものであり、URIの構成を正確に保つために行われています。文書内の該当部分が修正され、最新の情報が反映されています。変更が行われた具体的な行は、62行目におけるURIのバージョン部分です。

## articles/ai-services/openai/how-to/reinforcement-fine-tuning.md{#item-e8028c}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Customize o4-mini model with Azure OpenAI and reinforcement fine-tuning'
+title: 'Customize o4-mini model with Azure OpenAI and reinforcement fine-tuning (Preview)'
 description: Learn how to use reinforcement fine-tuning with Azure OpenAI
 manager: nitinme
 ms.service: azure-ai-openai
@@ -10,7 +10,7 @@ author: mrbullwinkle
 ms.author: mbullwin
 ---
 
-# Reinforcement fine-tuning (RFT) with Azure OpenAI o4-mini
+# Reinforcement fine-tuning (RFT) with Azure OpenAI o4-mini (Preview)
 
 Reinforcement fine-tuning (RFT) is a technique for improving reasoning models like o4-mini by training them through a reward-based process, rather than relying only on labeled data. By using feedback or "rewards" to guide learning, RFT helps models develop better reasoning and problem-solving skills, especially in cases where labeled examples are limited or complex behaviors are desired.
 
@@ -404,4 +404,4 @@ We also provide a grader check API that you can use to check the validity of you
 
 Aim for a few hundred examples initially and consider scaling up to around 1,000 examples if necessary. The dataset should be balanced, in terms of classes predicted, to avoid bias and ensure generalization.
 
-For the prompts, make sure to provide clear and detailed instructions, including specifying the response format and any constraints on the outputs (e.g. minimum length for explanations, only respond with true/false etc.)
\ No newline at end of file
+For the prompts, make sure to provide clear and detailed instructions, including specifying the response format and any constraints on the outputs (e.g. minimum length for explanations, only respond with true/false etc.)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "強化ファインチューニングのプレビュー版を明示"
}
```

### Explanation
この変更は、Azure OpenAIを使用した強化ファインチューニングに関するドキュメントのタイトルおよび見出しに「(Preview)」という表記を追加したものです。具体的には、タイトルが「Customize o4-mini model with Azure OpenAI and reinforcement fine-tuning」から「Customize o4-mini model with Azure OpenAI and reinforcement fine-tuning (Preview)」に変更され、見出しも同様に更新されました。この変更は、ユーザーに対してこの機能がプレビュー版であることを明確に示すことを目的としています。また、ドキュメントの内容については、強化ファインチューニングの手法に関する詳細な説明は維持されていますが、その周辺情報が明確化された形となります。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -25,6 +25,7 @@ manager: nitinme
 | `gpt-4.1` (2025-04-14) | North Central US <br> Sweden Central | ✅ | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text & Vision to Text |
 | `gpt-4.1-mini` (2025-04-14) | North Central US <br> Sweden Central | ✅ | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text to Text |
 | `gpt-4.1-nano` (2025-04-14) | North Central US <br> Sweden Central | ✅ | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 32,768 | May 2024 | Text to Text |
+| `o4-mini` (2025-04-16) | East US2 <br> Sweden Central | - | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text to Text |
 
 > [!NOTE]
 > **Global** training (in Public Preview) provides [more affordable](https://aka.ms/aoai-pricing) training per-token, but does not offer [data residency](https://aka.ms/data-residency). It is currently available to Azure OpenAI resources in the following regions, with more regions coming soon:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "o4-miniモデルの情報を追加"
}
```

### Explanation
この変更では、Azure OpenAIのファインチューニングモデルに関するドキュメントに、新しいモデル「o4-mini」の情報が追加されました。モデルの詳細には、リリース日（2025年4月16日）、利用可能なリージョン（East US2およびSweden Central）、入力トークン数（128,000）、出力トークン数（16,384）、トレーニング例のコンテキスト長（65,536）が含まれています。これにより、利用者はo4-miniモデルの特性を理解しやすくなり、ファインチューニングに関する選択肢が増えることになります。この追加情報は、ユーザーがモデルを選択する際に役立つ重要な要素となります。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -115,7 +115,7 @@ The first step is to confirm you model choice and the training method. Not all m
 
 - **Supervised Fine Tuning** (SFT): supported by all non-reasoning models.
 - **Direct Preference Optimization (Preview)** ([DPO](../how-to/fine-tuning-direct-preference-optimization.md)): supported by GPT-4o.
-- **Reinforcement Fine Tuning (Preview)** (RFT): supported by reasoning models, like o4-mini.
+- **Reinforcement Fine Tuning (Preview)** ([RFT](../how-to/reinforcement-fine-tuning.md)): supported by reasoning models, like o4-mini.
 
 When selecting the model, you may also select a [previously fine-tuned model](#continuous-fine-tuning).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "強化ファインチューニングのリンクを追加"
}
```

### Explanation
この変更では、強化ファインチューニング（RFT）に関する情報の表記が改善され、具体的には「Reinforcement Fine Tuning (Preview)」の後にリンクが追加されました。これにより、ユーザーはRFTの詳細なガイドを直接参照できるようになり、理解を深めることが可能になります。具体的に、RFTは推論モデルであるo4-miniによってサポートされています。このリンクの追加は、文書の情報をより充実させ、ユーザーにとっての利便性を向上させる要素といえます。全体的には、文書の一貫性と利用価値が向上したことになります。

## articles/ai-services/openai/realtime-audio-quickstart.md{#item-727df8}

<details>
<summary>Diff</summary>
````diff
@@ -62,3 +62,4 @@ Support for the Realtime API was first added in API version `2024-10-01-preview`
 * Learn more about [How to use the Realtime API](./how-to/realtime-audio.md)
 * See the [Realtime API reference](./realtime-audio-reference.md)
 * Learn more about Azure OpenAI [quotas and limits](quotas-limits.md)
+* Learn more about [Language and voice support for the Speech service](../../ai-services/speech-service/language-support.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "音声サービスの言語および音声サポートに関するリンクを追加"
}
```

### Explanation
この変更では、「Realtime API」に関するクイックスタートガイドに、新たに音声サービスの言語および音声サポートに関するリンクが追加されました。このリンクにより、ユーザーは音声サービスがどの言語や声をサポートしているかを簡単に確認できるようになり、Realtime APIの使用における理解が深まります。具体的には、APIが利用可能な言語や音声のオプションに対する情報提供が強化されたことで、開発者やユーザーがよりスムーズにサービスを活用できるようになっています。全体的に、情報の補完とユーザー体験の向上に寄与する変更です。


