---
date: '2025-02-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ea9b000...MicrosoftDocs:22af4d0
summary: このドキュメントでは、Azure OpenAIに関連するモデル情報が大幅に更新されたことが強調されています。主な変更点として、古いモデルの削除、新たなファインチューニングデータ要件の明確化、そして新モデルへの対応が挙げられます。特に「Conversational
  Chat」に関連するデータ要件が更新され、地域サポート情報も見直されています。リタイアメント日付の変更もあり、それに伴う計画調整が必要です。これにより、ユーザーはより効果的にAIサービスを利用できるようになります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ea9b000...MicrosoftDocs:22af4d0){target="_blank"}

# Highlights
このドキュメントの更新では、Azure OpenAIに関連するモデル情報が最新の状態に合わせて大幅に更新されています。特に、古いモデル情報（例えば、`babbage-002`や`davinci-002`のようなモデル）の削除、ファインチューニングに必要なデータ要件の明確化、新しいモデル（例えば、`GPT-4o`や`GPT-4o-mini`といったモデル）への対応が焦点です。また、モデルの地域サポート情報が全面的に見直されました。

## New features
- ファインチューニングのデータ要件が「Conversational Chat」に更新。
- 新モデル（`GPT-4o`や`GPT-4o-mini`）の地域サポート情報を追加。
- GPT-4 Turboクイックスタートガイドに新しいステップを追加。

## Breaking changes
- `babbage-002`および`davinci-002`に関する情報が削除され、これらはもはやファインチューニングや利用の対象として記載されていません。
- Microsoft Azure上のモデルのリタイアメント日付が変更されているため、それに基づく計画の調整が可能性として必要。

## Other updates
- 日付やテーブルフォーマットの単純な更新。
- 各ドキュメントにおける情報の整理や明確化。

# Insights
この一連のドキュメント更新は、OpenAIモデルのサポート体制の最新情報を反映し、ユーザーや企業がより効果的にこれらのAIサービスを使えるようにするためのものです。特に注目すべきは、新しいモデルに対応している点と、古いモデル情報を削除することでドキュメント自体が洗練されたことです。

ファインチューニングにおけるデータ要件が「Conversational Chat」に更新されたことは、対話型AIの利用が増えていることを示しています。これにより、ユーザーはより具体的なデータ提供が求められるかもしれませんが、それが成功すれば、より適切にチューニングされたモデルを手に入れることができます。

さらに、モデルリタイアメント日付の更新は、ユーザーが自分のアプリケーションが影響を受けないように計画を調整するための重要な指針です。リタイアメントスケジュールを確認し、モデルの切り替えや調整を計画することが推奨されます。

地域サポートの情報更新は、特定のAzureリージョンでのモデル利用可能性を明確にするための重要な情報です。企業はこの情報を元に、使用する地域に応じたアプリケーションの展開戦略を最適化できます。

これらの更新を通じて、ユーザーはますます効率的にAzure OpenAIサービスを利用するなり、最新のモデルへの移行がしやすくなることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [fine-tuning-considerations.md](#item-71d8ac) | minor update | ファインチューニングに関するデータ要件の更新 | modified | 4 | 4 | 8 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルのリタイアメント日付およびアップグレード情報の更新 | modified | 14 | 8 | 22 | 
| [models.md](#item-db2c37) | minor update | モデルに関する説明の簡素化 | modified | 0 | 3 | 3 | 
| [gpt-v-quickstart.md](#item-2a6183) | minor update | GPT-4 Turboのお知らせ文の更新と次のステップの追加 | modified | 2 | 1 | 3 | 
| [fine-tuning.md](#item-5c0e85) | minor update | デプロイ対象の明確化 | modified | 1 | 1 | 2 | 
| [fine-tune-models.md](#item-2aadea) | minor update | ファインチューニングモデルの更新日とモデルリストの簡略化 | modified | 1 | 3 | 4 | 
| [fine-tuning-openai-in-ai-studio.md](#item-723c8d) | minor update | 古いモデルの情報削除と簡素化 | modified | 0 | 54 | 54 | 
| [fine-tuning-python.md](#item-976f58) | minor update | 不要なモデルの削除とドキュメントの簡素化 | modified | 3 | 57 | 60 | 
| [fine-tuning-rest.md](#item-9add3e) | minor update | 古いモデルの情報削除とドキュメント簡素化 | modified | 1 | 66 | 67 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | 古いモデル情報の削除とドキュメントの簡素化 | modified | 0 | 64 | 64 | 
| [provisioned-global.md](#item-340884) | minor update | 新モデルの地域サポート情報の更新 | modified | 17 | 17 | 34 | 
| [standard-completions.md](#item-a9c095) | minor update | 標準的なコンプリートモデル情報の簡素化と更新 | modified | 5 | 6 | 11 | 
| [standard-global.md](#item-17a84b) | minor update | 標準グローバルモデルのサポート地域の情報更新 | modified | 26 | 27 | 53 | 
| [standard-image-generation.md](#item-dd78ea) | minor update | 画像生成モデルの地域サポート情報の更新 | modified | 6 | 6 | 12 | 
| [standard-models.md](#item-af04c4) | minor update | 標準モデルの地域サポート情報の更新 | modified | 23 | 23 | 46 | 
| [overview.md](#item-97d507) | minor update | ファインチューニングモデル情報の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/fine-tuning-considerations.md{#item-71d8ac}

<details>
<summary>Diff</summary>
````diff
@@ -79,10 +79,10 @@ Even with a great use case, fine-tuning is only as good as the quality of the da
 
 Another important point is even with high quality data if your data isn't in the necessary format for fine-tuning you'll need to commit engineering resources in order to properly format the data.
 
-| Data  | Babbage-002 <br> Davinci-002 | GPT-3.5-Turbo <br> GPT-4o & GPT-4o mini <br> GPT-4 |
-|---|---|---|
-| Volume | Thousands of Examples | Thousands of Examples |
-| Format | Prompt/Completion | Conversational Chat |
+| Data   | GPT-3.5-Turbo <br> GPT-4o & GPT-4o mini <br> GPT-4 |
+|---|---|
+| Volume  | Thousands of Examples |
+| Format | Conversational Chat |
 
 **If you are ready for fine-tuning you:**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関するデータ要件の更新"
}
```

### Explanation
このコードの変更は、ファインチューニングに関する文書内のデータ要件についての内容を更新したものです。具体的には、AIモデルに関連するデータの形式とボリュームに関する表が変更されています。以前は複数のモデル（Babbage-002、Davinci-002など）が含まれていましたが、変更後はGPT-3.5-Turbo、GPT-4oおよびGPT-4o mini、GPT-4のみに焦点を当てています。

テーブルの内容は以下のように変わりました：

- データ形式が「Prompt/Completion」から「Conversational Chat」に変更されました。
- モデル名がシンプルに整理され、より関連性の高い情報のみが列挙されています。

この更新は、ユーザーがファインチューニングを行う際のデータ要件を明確にし、より使いやすくするためのものです。変更は合計で8箇所行われており、インデントや改行を含めて、4箇所の追加と4箇所の削除がありました。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 01/15/2025
+ms.date: 02/06/2025
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -97,17 +97,19 @@ These models are currently available for use in Azure OpenAI Service.
 | `davinci-002` | 1 | Retirement Date: January 27, 2025 | |
 | `dall-e-2`| 2 | January 27, 2025 | `dalle-3` |
 | `dall-e-3` | 3 | No earlier than April 30, 2025 | |
-| `gpt-35-turbo` | 0301 | February 13, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
-| `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | February 13, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
-| `gpt-35-turbo` | 1106 | No earlier than March 31, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
+| `gpt-35-turbo` | 0301 | February 13, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
+| `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | February 13, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
+| `gpt-35-turbo` | 1106 | No earlier than March 31, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
 | `gpt-35-turbo` | 0125 | No earlier than May 31, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
 | `gpt-4` | turbo-2024-04-09 | No earlier than April 9, 2025 | `gpt-4o`|
-| `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>** | `gpt-4o`|
-| `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025 **<sup>1</sup>**  | `gpt-4o` |
-| `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than January 27, 2025  **<sup>1</sup>** | `gpt-4o`|
+| `gpt-4` | 1106-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025 **<sup>1</sup>** <br>Retirement date: February 28, 2025  | `gpt-4o`|
+| `gpt-4` | 0125-preview |To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025 **<sup>1</sup>** <br>Retirement date: February 28, 2025  | `gpt-4o` |
+| `gpt-4` | vision-preview | To be upgraded to `gpt-4` version: `turbo-2024-04-09`, starting no sooner than February 10, 2025  **<sup>1</sup>** <br>Retirement date: February 28, 2025 | `gpt-4o`|
 | `gpt-4o` | 2024-05-13 | No earlier than May 20, 2025 <br><br>Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. | |
+| `gpt-4o` | 2024-08-06 | No earlier than August 6, 2025  | |
+| `gpt-4o` | 2024-11-20 | No earlier than November 20, 2025  | |
 | `gpt-4o-mini` | 2024-07-18 | No earlier than July 18, 2025  | |
 | `gpt-4o-realtime-preview` | 2024-10-01 | No earlier than September 30, 2025  | `gpt-4o-realtime-preview` (version 2024-12-17) or `gpt-4o-mini-realtime-preview` (version 2024-12-17) |
 | `gpt-3.5-turbo-instruct` | 0914 | No earlier than April 1, 2025 |  |
@@ -126,7 +128,7 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Current default version | New default version | Default upgrade date |
 |---|---|---|---|
-| `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 13, 2025.|
+| `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on January 21, 2025.|
 |  `gpt-4o` | 2024-05-13 | 2024-08-06 | Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `2024-08-06`, starting on February 13, 2025. |
 
 ## Deprecated models
@@ -167,6 +169,10 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## February 6, 2025
+
+- Updates to `gpt-35-turbo`, `gpt-4` preview models, and `gpt-4o` models.
+
 ## January 9, 2025
 
 - `o1` added.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのリタイアメント日付およびアップグレード情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるモデルのリタイアメント日付と、デフォルトのアップグレードに関する情報を更新するものです。主な変更点として以下が挙げられます：

1. **日付の変更**: `gpt-35-turbo`モデルのアップグレード開始日が、元の2025年1月13日から2025年1月21日に変更されました。他のモデルに関しても同様の変更があり、投稿日付が更新されています。

2. **新しいモデル情報の追加**: `gpt-4`関連のプレビューモデルについて、リタイアメント日付が追加され、より詳細な情報が提供されています。これにより、顧客はこれらのモデルの使用に関する計画を立てやすくなります。

3. **テーブルの更新**: モデルの現在のバージョン、新しいデフォルトバージョン、そしてデフォルトのアップグレード日が含まれたテーブルが更新され、各モデルに対する最新の状況が明確に示されています。

この変更は、Azure OpenAIの利用者にとって重要な情報であり、計画や準備に役立つ内容となっています。合計で22箇所の変更が行われ、その中には14箇所の追加と8箇所の削除が含まれています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -320,7 +320,6 @@ These models can only be used with Embedding API requests.
 
 |  Model ID  | Max Request (characters) |
 |  --- | :---: |
-| dalle2 (preview)  | 1,000 |
 | dall-e-3  | 4,000 |
 
 # [Audio](#tab/standard-audio)
@@ -347,8 +346,6 @@ These models can only be used with Embedding API requests.
 
 ### Completions models
 
-`babbage-002` and `davinci-002` are not trained to follow instructions. Querying these base models should only be done as a point of reference to a fine-tuned version to evaluate the progress of your training.
-
 [!INCLUDE [Completions](../includes/model-matrix/standard-completions.md)]
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関する説明の簡素化"
}
```

### Explanation
このコードの変更は、OpenAIモデルに関するドキュメントの一部を簡素化するためのもので、具体的には不要な情報を削除しています。主な変更点は次の通りです：

1. **削除されたモデル情報**: `dalle2 (preview)`に関する情報が表から削除されており、これにより承認されたモデルに関する情報が整理されました。この結果、表では`dall-e-3`のモデルのみが残っており、リクエストの最大文字数が4,000文字であることが示されています。

2. **指示に従わないモデルの説明の削除**: `babbage-002`および`davinci-002`に関する説明が削除され、これらの基本モデルが指示には従わないことや、ファインチューニングされたバージョンの参考としてのみ使用すべきであるという情報もなくなりました。

3. **内容の簡素化**: 全体的に、不要な説明が削除されていることで、文書がより明瞭になり、必要な情報を探しやすくなっています。

合計で3箇所の変更があり、すべて削除が行われており、選択されたモデルに関する情報を簡潔に保っています。これにより、ユーザーは重要な情報に迅速にアクセスできるようになります。

## articles/ai-services/openai/gpt-v-quickstart.md{#item-2a6183}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ Get started using GPT-4 Turbo with images with the Azure OpenAI Service.
 > [!NOTE]
 > **Model choice**
 >
-> The latest vision-capable models are `gpt-4o` and `gpt-4o mini`. These are in public preview. The latest available GA model is `gpt-4` version `turbo-2024-04-09`.
+> The latest vision-capable models are `gpt-4o` and `gpt-4o mini`. These models are in public preview. The latest available GA model is `gpt-4` version `turbo-2024-04-09`.
 
 ::: zone pivot="ai-foundry-portal"
 
@@ -60,6 +60,7 @@ Get started using GPT-4 Turbo with images with the Azure OpenAI Service.
 
 ## Next steps
 
+* [Get started with multimodal vision chat apps using Azure OpenAI](/azure/developer/ai/get-started-app-chat-vision?tabs=github-codespaces) AI App template
 * Learn more about these APIs in the [Vision-enabled models how-to guide](./gpt-v-quickstart.md)
 * [GPT-4 Turbo with Vision frequently asked questions](./faq.yml#gpt-4-turbo-with-vision)
 * [GPT-4 Turbo with Vision API reference](https://aka.ms/gpt-v-api-ref)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turboのお知らせ文の更新と次のステップの追加"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるGPT-4 Turboのクイックスタートガイドを更新するもので、いくつかの小さな変更が含まれています。主な変更点は以下の通りです：

1. **説明文の修正**: 「最新のビジョン対応モデルは`gpt-4o`および`gpt-4o mini`であり、これらはパブリックプレビュー中です。」という部分が修正され、モデル名の後に「これらのモデルはパブリックプレビュー中です。」という文が追加されました。この変更により、モデルについての情報が一層明確になっています。

2. **次のステップの追加**: ユーザーが次にどのようなステップを踏むべきかを示すリストが更新され、特に「[Get started with multimodal vision chat apps using Azure OpenAI]」という新しいリンクが追加され、マルチモーダルビジョンチャットアプリの開発に関する情報が強調されています。

3. **全体の整理**: 合計で3箇所の変更が行われ、そのうち2箇所は新しいテキストの追加であり、1箇所は既存の情報の微調整です。この更新により、ドキュメントの情報がより役立つものとなり、ユーザーの理解が深まることを目的としています。

これにより、クイックスタートガイドは最新の情報を反映し、ユーザーが次のアクションを容易に見つけられるようになっています。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ We use LoRA, or low rank approximation, to fine-tune models in a way that reduce
 Azure OpenAI fine-tuning supports [global standard deployments](./deployment-types.md#global-standard) in East US2, North Central US, and Sweden Central for:
 
 - `gpt-4o-mini-2024-07-18`
-- `gpt-4o-2024-08-06` (New deployments aren't available until January 2025)
+- `gpt-4o-2024-08-06`
 
 Global standard fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイ対象の明確化"
}
```

### Explanation
このコードの変更は、Azure OpenAIのファインチューニングに関するドキュメントを更新するもので、以下の小さな変更が含まれています。

1. **モデル名の修正**: `gpt-4o-2024-08-06` 行の先頭にある「-」が削除され、リストの形式が一貫性を持つように整理されました。これにより、ドキュメント内でモデルが明確に列挙されるようになります。

2. **新しいデプロイメントの可用性に関する情報**: 新しいデプロイメントの待機期間についてのコメントが削除され、これにより最新の情報提供が強調されています。これまでは「新しいデプロイメントは2025年1月まで利用できません」との文が削除され、現在利用可能なモデルにフォーカスが当たっています。

この変更により、ユーザーがファインチューニングを行う際に利用できるモデルに関する情報が更新され、より明確かつ分かりやすくなっています。全体で2箇所の変更があり、ドキュメントの整合性と可読性が向上しています。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 ms.author: mbullwin 
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/31/2024
+ms.date: 02/06/2025
 manager: nitinme
 ---
 
@@ -17,8 +17,6 @@ manager: nitinme
 
 |  Model ID  | Fine-tuning regions | Max request (tokens) | Training Data (up to) |
 |  --- | --- | :---: | :---: |
-| `babbage-002` | North Central US <br> Sweden Central  <br> Switzerland West | 16,384 | Sep 2021 |
-| `davinci-002` | North Central US <br> Sweden Central  <br> Switzerland West | 16,384 | Sep 2021 |
 | `gpt-35-turbo` (0613) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 4,096 | Sep 2021 |
 | `gpt-35-turbo` (1106) | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | Input: 16,385<br> Output: 4,096 |  Sep 2021|
 | `gpt-35-turbo` (0125)  | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 16,385 | Sep 2021 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングモデルの更新日とモデルリストの簡略化"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスのファインチューニングモデルに関連するドキュメントを更新するもので、具体的には以下の点が改訂されています：

1. **更新日付の変更**: `ms.date`フィールドの値が「10/31/2024」から「02/06/2025」に更新されました。これにより、ドキュメントの情報がより最新のものとして反映されています。

2. **モデル情報の簡略化**: `babbage-002`および`davinci-002`の行が削除され、これに伴いそれらのモデルがfine-tuning可能な領域から除外されました。これにより、現在の主要なファインチューニングモデルはより焦点が絞られた形でリストされています。

3. **全体の整理**: 用語やFormatの整合性を持たせるため、残りのモデルのリストが更新され、管理者情報については変更がありませんが、その他の行が簡潔になりました。

この変更によって、ファインチューニングに利用できるモデルの情報はより明確で、ドキュメントの読みやすさと利便性が向上しています。

## articles/ai-services/openai/includes/fine-tuning-openai-in-ai-studio.md{#item-723c8d}

<details>
<summary>Diff</summary>
````diff
@@ -28,8 +28,6 @@ ms.custom: include, build-2024
 
 The following models support fine-tuning:
 
-- `babbage-002`
-- `davinci-002`
 - `gpt-35-turbo` (0613)
 - `gpt-35-turbo` (1106)
 - `gpt-35-turbo` (0125)
@@ -64,10 +62,6 @@ Take a moment to review the fine-tuning workflow for using Azure AI Foundry:
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
-Different model types require a different format of training data.
-
-# [chat completion models](#tab/turbo)
-
 The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo-0613` the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
 If you would like a step-by-step walk-through of fine-tuning a `gpt-35-turbo-0613` model please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
@@ -104,54 +98,6 @@ The more training examples you have, the better. Fine tuning jobs will not proce
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
 
-# [babbage-002/davinci-002](#tab/completionfinetuning)
-
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document in which each line represents a single prompt-completion pair. The OpenAI command-line interface (CLI) includes [a data preparation tool](#openai-cli-data-preparation-tool) that validates, gives suggestions, and reformats your training data into a JSONL file ready for fine-tuning.
-
-```json
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-```
-
-In addition to the JSONL format, training and validation data files must be encoded in UTF-8 and include a byte-order mark (BOM). The file must be less than 512 MB in size.
-
-### Create your training and validation datasets
-
-Designing your prompts and completions for fine-tuning is different from designing your prompts for use with any of [our GPT-3 base models](../concepts/legacy-models.md#gpt-3-models). Prompts for completion calls often use either detailed instructions or few-shot learning techniques, and consist of multiple examples. For fine-tuning, each training example should consist of a single input prompt and its desired completion output. You don't need to give detailed instructions or multiple completion examples for the same prompt.
-
-The more training examples you have, the better. The minimum number of training examples is 10, but such a small number of examples is often not enough to noticeably influence model responses. OpenAI states it's best practice to have at least 50 high quality training examples. However, it is entirely possible to have a use case that might require 1,000's of high quality training examples to be successful.
-
-In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
-
-### OpenAI CLI data preparation tool
-
-OpenAI's CLI data preparation tool was developed for the previous generation of fine-tuning models to assist with many of the data preparation steps. This tool will only work for data preparation for models that work with the completion API like `babbage-002` and `davinci-002`. The tool validates, gives suggestions, and reformats your data into a JSONL file ready for fine-tuning.
-
-To install the OpenAI CLI, run the following Python command:
-
-```console
-pip install openai==0.28.1
-```
-
-To analyze your training data with the data preparation tool, run the following Python command. Replace the _\<LOCAL_FILE>_ argument with the full path and file name of the training data file to analyze:
-
-```console
-openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
-```
-
-This tool accepts files in the following data formats, if they contain a prompt and a completion column/key:
-
-- Comma-separated values (CSV)
-- Tab-separated values (TSV)
-- Microsoft Excel workbook (XLSX)
-- JavaScript Object Notation (JSON)
-- JSON Lines (JSONL)
-
-After it guides you through the process of implementing suggested changes, the tool reformats your training data and saves output into a JSONL file ready for fine-tuning.
-
----
-
 ## Create your fine-tuned model
 
 To fine-tune an Azure OpenAI model in an existing Azure AI Foundry project, follow these steps:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "古いモデルの情報削除と簡素化"
}
```

### Explanation
このコードの変更では、Azure OpenAIに関するドキュメントが大幅に修正され、以下のような主要な改訂が行われました：

1. **古いモデルの削除**: `babbage-002`および`davinci-002`の関連情報がすべて削除されました。これにより、現在サポートされているファインチューニングモデルは`gpt-35-turbo`シリーズに限定され、より鮮明な焦点が当てられています。

2. **情報の簡素化**: ドキュメント内に存在した詳細なデータ処理手順や形式についての説明が削除され、全体的にテキスト量が減少しました。特に、トレーニングデータや検証データに関する大規模なセクションがなくなり、情報が整理されています。

3. **データ準備ツールの情報削除**: OpenAI CLIデータ準備ツールに関する情報も削除され、古いモデルに関連するデータ準備の手順が省かれています。この変更により、読者にとっての情報の関連性が向上します。

この変更の結果、ドキュメントは今後のサポートされるモデルに偏った焦点を持ち、ファインチューニング作業における無駄な情報を排除する形で、利用者が必要とする情報を簡潔に提供するようになりました。

## articles/ai-services/openai/includes/fine-tuning-python.md{#item-976f58}

<details>
<summary>Diff</summary>
````diff
@@ -26,8 +26,6 @@ ms.author: mbullwin
 
 The following models support fine-tuning:
 
-- `babbage-002`
-- `davinci-002`
 - `gpt-35-turbo` (0613)
 - `gpt-35-turbo` (1106)
 - `gpt-35-turbo` (0125)
@@ -60,10 +58,6 @@ Take a moment to review the fine-tuning workflow for using the Python SDK with A
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
-Different model types require a different format of training data.
-
-# [chat completion models](#tab/turbo)
-
 The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo-0613` the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
 If you would like a step-by-step walk-through of fine-tuning a `gpt-35-turbo-0613` please refer to the [Azure OpenAI fine-tuning tutorial](../tutorials/fine-tune.md)
@@ -100,54 +94,6 @@ The more training examples you have, the better. Fine tuning jobs will not proce
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
 
-# [babbage-002/davinci-002](#tab/completionfinetuning)
-
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document in which each line represents a single prompt-completion pair. The OpenAI command-line interface (CLI) includes [a data preparation tool](#openai-cli-data-preparation-tool) that validates, gives suggestions, and reformats your training data into a JSONL file ready for fine-tuning.
-
-```json
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-```
-
-In addition to the JSONL format, training and validation data files must be encoded in UTF-8 and include a byte-order mark (BOM). The file must be less than 512 MB in size.
-
-### Create your training and validation datasets
-
-Designing your prompts and completions for fine-tuning is different from designing your prompts for use with any of [our GPT-3 base models](../concepts/legacy-models.md#gpt-3-models). Prompts for completion calls often use either detailed instructions or few-shot learning techniques, and consist of multiple examples. For fine-tuning, each training example should consist of a single input prompt and its desired completion output. You don't need to give detailed instructions or multiple completion examples for the same prompt.
-
-The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number is not enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful.
-
-In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
-
-### OpenAI CLI data preparation tool
-
-OpenAI's CLI data preparation tool was developed for the previous generation of fine-tuning models to assist with many of the data preparation steps. This tool will only work for data preparation for models that work with the completion API like `babbage-002` and `davinci-002`. The tool validates, gives suggestions, and reformats your data into a JSONL file ready for fine-tuning.
-
-To install the OpenAI CLI, run the following Python command:
-
-```console
-pip install openai==0.28.1
-```
-
-To analyze your training data with the data preparation tool, run the following Python command. Replace the _\<LOCAL_FILE>_ argument with the full path and file name of the training data file to analyze:
-
-```console
-openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
-```
-
-This tool accepts files in the following data formats, if they contain a prompt and a completion column/key:
-
-- Comma-separated values (CSV)
-- Tab-separated values (TSV)
-- Microsoft Excel workbook (XLSX)
-- JavaScript Object Notation (JSON)
-- JSON Lines (JSONL)
-
-After it guides you through the process of implementing suggested changes, the tool reformats your training data and saves output into a JSONL file ready for fine-tuning.
-
----
-
 ## Upload your training data
 
 The next step is to either choose existing prepared training data or upload new prepared training data to use when customizing your model. After you prepare your training data, you can upload your files to the service. There are two ways to upload training data:
@@ -209,7 +155,7 @@ import os
 openai.api_key = os.getenv("AZURE_OPENAI_API_KEY") 
 openai.api_base =  os.getenv("AZURE_OPENAI_ENDPOINT")
 openai.api_type = 'azure'
-openai.api_version = '2024-02-01' # This API version or later is required to access fine-tuning for turbo/babbage-002/davinci-002
+openai.api_version = '2024-02-01' # This API version or later is required
 
 training_file_name = 'training_set.jsonl'
 validation_file_name = 'validation_set.jsonl'
@@ -302,7 +248,7 @@ from openai import AzureOpenAI
 client = AzureOpenAI(
   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-02-01"  # This API version or later is required to access fine-tuning for turbo/babbage-002/davinci-002
+  api_version="2024-02-01"  # This API version or later is required
 )
 
 client.fine_tuning.jobs.create(
@@ -580,7 +526,7 @@ az cognitiveservices account deployment create
 
 ## Use a deployed customized model
 
-After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry](https://ai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models. For fine-tuned `babbage-002` and `davinci-002` models you will use the Completions playground and the Completions API. For fine-tuned `gpt-35-turbo-0613` models you will use the Chat playground and the Chat completion API.
+After your custom model deploys, you can use it like any other deployed model. You can use the **Chat Playground** in [Azure AI Foundry](https://ai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
 
 # [OpenAI Python 1.x](#tab/python-new)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "不要なモデルの削除とドキュメントの簡素化"
}
```

### Explanation
このコードの変更では、Azure OpenAIに関するPython SDKを用いたファインチューニングに関するドキュメントが大幅に改訂され、以下の重要な修正が含まれています：

1. **古いモデルの情報削除**: `babbage-002`および`davinci-002`に関する情報がドキュメントから削除され、現在サポートされているモデルが`gpt-35-turbo`シリーズのみに焦点を当てられるようになりました。これにより、読者は最新の情報に基づいてより適切な選択ができるようになります。

2. **冗長な情報の削除**: トレーニングデータのフォーマットに関する詳細や、以前のモデルに関連する情報が削除されました。特に、データ準備ツールやその利用法に関する長文が簡素化され、必要最小限の情報のみが残されています。

3. **ワークフローの明確化**: ファインチューニングのためのワークフローや、トレーニング例の重要性に関する説明が整理されました。特に、トレーニングと検証データの要件に関する部分が見やすくなり、より効果的なモデル構築のためのガイダンスが与えられています。

4. **APIバージョンの更新**: コードスニペット内でのAPIバージョンに関するコメントが簡素化され、`turbo/babbage-002/davinci-002`という表現が削除されています。これにより、特定のバージョンに対する依存関係が低減されています。

これらの変更により、ドキュメントは最新のモデルに特化し、情報が整理され、読みやすく、実用的なものに改善されました。

## articles/ai-services/openai/includes/fine-tuning-rest.md{#item-9add3e}

<details>
<summary>Diff</summary>
````diff
@@ -25,8 +25,6 @@ ms.author: mbullwin
 
 The following models support fine-tuning:
 
-- `babbage-002`
-- `davinci-002`
 - `gpt-35-turbo` (0613)
 - `gpt-35-turbo` (1106)
 - `gpt-35-turbo` (0125)
@@ -59,10 +57,6 @@ Take a moment to review the fine-tuning workflow for using the REST APIS and Pyt
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
-Different model types require a different format of training data.
-
-# [chat completion models](#tab/turbo)
-
 The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo-0613` and other related models, the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
 If you would like a step-by-step walk-through of fine-tuning a `gpt-35-turbo-0613` please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
@@ -100,71 +94,12 @@ The more training examples you have, the better. Fine tuning jobs will not proce
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data without first pruning the dataset for only the highest quality examples, you could end up with a model that performs much worse than expected.
 
-# [babbage-002/davinci-002](#tab/completionfinetuning)
-
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document in which each line represents a single prompt-completion pair. The OpenAI command-line interface (CLI) includes [a data preparation tool](#openai-cli-data-preparation-tool) that validates, gives suggestions, and reformats your training data into a JSONL file ready for fine-tuning.
-
-```json
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-```
-
-In addition to the JSONL format, training and validation data files must be encoded in UTF-8 and include a byte-order mark (BOM). The file must be less than 512 MB in size.
-
-### Create your training and validation datasets
-
-Designing your prompts and completions for fine-tuning is different from designing your prompts for use with any of [our GPT-3 base models](../concepts/legacy-models.md#gpt-3-models). Prompts for completion calls often use either detailed instructions or few-shot learning techniques, and consist of multiple examples. For fine-tuning, each training example should consist of a single input prompt and its desired completion output. You don't need to give detailed instructions or multiple completion examples for the same prompt.
-
-The more training examples you have, the better. Fine tuning jobs will not proceed without at least 10 training examples, but such a small number is not enough to noticeably influence model responses. It is best practice to provide hundreds, if not thousands, of training examples to be successful.
-
-In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data without first pruning the dataset for only the highest quality examples, you could end up with a model that performs much worse than expected.
-
-### OpenAI CLI data preparation tool
-
-OpenAI's CLI data preparation tool was developed for the previous generation of fine-tuning models to assist with many of the data preparation steps. This tool will only work for data preparation for models that work with the completion API like `babbage-002` and `davinci-002`. The tool validates, gives suggestions, and reformats your data into a JSONL file ready for fine-tuning.
-
-To install the OpenAI CLI, run the following Python command:
-
-```console
-pip install openai==0.28.1
-```
-
-To analyze your training data with the data preparation tool, run the following Python command. Replace the _\<LOCAL_FILE>_ argument with the full path and file name of the training data file to analyze:
-
-```console
-openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
-```
-
-This tool accepts files in the following data formats, if they contain a prompt and a completion column/key:
-
-- Comma-separated values (CSV)
-- Tab-separated values (TSV)
-- Microsoft Excel workbook (XLSX)
-- JavaScript Object Notation (JSON)
-- JSON Lines (JSONL)
-
-After it guides you through the process of implementing suggested changes, the tool reformats your training data and saves output into a JSONL file ready for fine-tuning.
-
----
-
 ### Select the base model
 
 The first step in creating a custom model is to choose a base model. The **Base model** pane lets you choose a base model to use for your custom model. Your choice influences both the performance and the cost of your model.
 
 Select the base model from the **Base model type** dropdown, and then select **Next** to continue.
 
-You can create a custom model from one of the following available base models:
-
-- `babbage-002`
-- `davinci-002`
-- `gpt-35-turbo` (0613)
-- `gpt-35-turbo` (1106)
-- `gpt-35-turbo` (0125)
-- `gpt-4` (0613)
-- `gpt-4o` (2024-08-06)
-- `gpt-4o-mini` (2023-07-18)
-
 Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
 
 :::image type="content" source="../media/fine-tuning/models.png" alt-text="Screenshot of model options with a custom fine-tuned model." lightbox="../media/fine-tuning/models.png":::
@@ -373,7 +308,7 @@ az cognitiveservices account deployment create
 
 ## Use a deployed customized model
 
-After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry](https://ai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models. For fine-tuned `babbage-002` and `davinci-002` models you'll use the Completions playground and the Completions API. For fine-tuned `gpt-35-turbo-0613` models you'll use the Chat playground and the Chat completion API.
+After your custom model deploys, you can use it like any other deployed model. You can use the **Chat Playgrounds** in [Azure AI Foundry](https://ai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models.
 
 ```bash
 curl $AZURE_OPENAI_ENDPOINT/openai/deployments/<deployment_name>/chat/completions?api-version=2023-05-15 \
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "古いモデルの情報削除とドキュメント簡素化"
}
```

### Explanation
このコードの変更では、Azure OpenAIに関するREST APIを用いたファインチューニングに関するドキュメントが改訂され、以下のポイントが主に修正されています：

1. **古いモデルの情報削除**: `babbage-002`および`davinci-002`の情報が削除され、現在サポートされているモデルが`gpt-35-turbo`シリーズに焦点を当てられています。これにより、ユーザーは最新のモデルに関する情報に基づいて手順を実行できます。

2. **冗長な説明の削除**: トレーニングデータフォーマットに関する詳細な手順が削除され、特にJSON Line（JSONL）フォーマットに関する不必要な重複が取り除かれています。これにより、必要な情報がわかりやすく整理されています。

3. **API使用の明確化**: ドキュメント全体にわたってREST APIを使用する際のガイドが更新されており、ファインチューニングされたモデルの使用に関する情報がより明確になっています。特に、カスタムモデルのデプロイやその利用方法についての説明が改善されています。

4. **プレイグラウンドの用語修正**: 「Playgrounds」という表現が「Chat Playgrounds」に変更され、ユーザーに提供されるインターフェイスの整合性が保たれています。

これらの改訂により、ドキュメントは最新の推奨事項に基づく明確かつ簡潔な内容になり、ユーザーが効果的にAzure OpenAIを利用できるよう支援しています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -23,8 +23,6 @@ ms.author: mbullwin
 
 The following models support fine-tuning:
 
-- `babbage-002`
-- `davinci-002`
 - `gpt-35-turbo` (0613)
 - `gpt-35-turbo` (1106)
 - `gpt-35-turbo` (0125)
@@ -39,7 +37,6 @@ Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{
 
 Consult the [models page](../concepts/models.md#fine-tuning-models) to check which regions currently support fine-tuning.
 
-
 ## Review the workflow for Azure AI Foundry portal
 
 Take a moment to review the fine-tuning workflow for using Azure AI Foundry portal:
@@ -60,10 +57,6 @@ Take a moment to review the fine-tuning workflow for using Azure AI Foundry port
 
 Your training data and validation data sets consist of input and output examples for how you would like the model to perform.
 
-Different model types require a different format of training data.
-
-# [chat completion models](#tab/turbo)
-
 The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo` (all versions), `gpt-4`, `gpt-4o`, and `gpt-4o-mini`, the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
 If you would like a step-by-step walk-through of fine-tuning a `gpt-4o-mini` (2024-07-18) model please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
@@ -100,54 +93,6 @@ The more training examples you have, the better. Fine tuning jobs will not proce
 
 In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
 
-# [babbage-002/davinci-002](#tab/completionfinetuning)
-
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document in which each line represents a single prompt-completion pair. The OpenAI command-line interface (CLI) includes [a data preparation tool](#openai-cli-data-preparation-tool) that validates, gives suggestions, and reformats your training data into a JSONL file ready for fine-tuning.
-
-```json
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
-```
-
-In addition to the JSONL format, training and validation data files must be encoded in UTF-8 and include a byte-order mark (BOM). The file must be less than 512 MB in size.
-
-### Create your training and validation datasets
-
-Designing your prompts and completions for fine-tuning is different from designing your prompts for use with any of [our GPT-3 base models](../concepts/legacy-models.md#gpt-3-models). Prompts for completion calls often use either detailed instructions or few-shot learning techniques, and consist of multiple examples. For fine-tuning, each training example should consist of a single input prompt and its desired completion output. You don't need to give detailed instructions or multiple completion examples for the same prompt.
-
-The more training examples you have, the better. The minimum number of training examples is 10, but such a small number of examples is often not enough to noticeably influence model responses. OpenAI states it's best practice to have at least 50 high quality training examples. However, it is entirely possible to have a use case that might require 1,000's of high quality training examples to be successful.
-
-In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples you could end up with a model that performs much worse than expected.
-
-### OpenAI CLI data preparation tool
-
-OpenAI's CLI data preparation tool was developed for the previous generation of fine-tuning models to assist with many of the data preparation steps. This tool will only work for data preparation for models that work with the completion API like `babbage-002` and `davinci-002`. The tool validates, gives suggestions, and reformats your data into a JSONL file ready for fine-tuning.
-
-To install the OpenAI CLI, run the following Python command:
-
-```console
-pip install openai==0.28.1
-```
-
-To analyze your training data with the data preparation tool, run the following Python command. Replace the _\<LOCAL_FILE>_ argument with the full path and file name of the training data file to analyze:
-
-```console
-openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
-```
-
-This tool accepts files in the following data formats, if they contain a prompt and a completion column/key:
-
-- Comma-separated values (CSV)
-- Tab-separated values (TSV)
-- Microsoft Excel workbook (XLSX)
-- JavaScript Object Notation (JSON)
-- JSON Lines (JSONL)
-
-After it guides you through the process of implementing suggested changes, the tool reformats your training data and saves output into a JSONL file ready for fine-tuning.
-
----
-
 ## Use the Create custom model wizard
 
 Azure AI Foundry portal provides the **Create custom model** wizard, so you can interactively create and train a fine-tuned model for your Azure resource.
@@ -166,15 +111,6 @@ The first step in creating a custom model is to choose a base model. The **Base
 
 Select the base model from the **Base model type** dropdown, and then select **Next** to continue.
 
-You can create a custom model from one of the following available base models:
-
-- `babbage-002`
-- `davinci-002`
-- `gpt-35-turbo` (0613)
-- `gpt-35-turbo` (1106)
-- `gpt-35-turbo` (0125)
-- `gpt-4` (0613)
-
 - Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
 
 :::image type="content" source="../media/fine-tuning/models.png" alt-text="Screenshot of model options with a custom fine-tuned model." lightbox="../media/fine-tuning/models.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "古いモデル情報の削除とドキュメントの簡素化"
}
```

### Explanation
このコードの変更では、Azure OpenAIに関するファインチューニングスタジオに関するドキュメントが改訂され、以下の主要な修正が行われています：

1. **古いモデルの情報削除**: `babbage-002`および`davinci-002`に関する情報が削除され、現在サポートされているモデルが`gpt-35-turbo`シリーズと新しい`gpt-4`モデルに焦点が当てられています。これにより、ユーザーは最新のファインチューニングのオプションに基づいて作業を進めることができます。

2. **冗長なセクションの削除**: トレーニングデータに関する説明が簡素化され、特定のモデルに関する詳細な要件や、プロンプトとコンプリートペアの形式に関する冗長な部分が削除されました。これにより、ドキュメントがコンパクトかつ理解しやすくなっています。

3. **ワークフローのクリアな提示**: Azure AI Foundryポータルでのファインチューニングワークフローに関する情報が整理され、段階的に説明されています。特にトレーニングと検証データセットがどのように準備されるかについてのガイダンスが改善されています。

4. **カスタムモデル作成ツールに関する改善**: カスタムモデル作成ウィザードに関する情報が更新され、ユーザーが簡単にカスタムモデルを作成できる手順が明確化されています。

これらの変更により、ドキュメントはよりユーザーフレンドリーになり、最新の情報が簡潔かつ効果的に伝わるようになっています。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -6,34 +6,34 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 01/15/2025
+ms.date: 02/06/2025
 ---
 
 | **Region**     | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
 |:-------------------|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
 | australiaeast      | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                       | ✅                       | -                      | ✅                            |
-| canadacentral      | ✅                       | ✅                       | -                      | ✅                            |
+| brazilsouth        | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadacentral      | ✅                       | ✅                       | ✅                       | ✅                            |
 | canadaeast         | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus             | ✅                       | ✅                       | ✅                       | ✅                            |
 | eastus2            | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                       | ✅                       | -                      | ✅                            |
-| germanywestcentral | ✅                       | ✅                       | -                      | ✅                            |
-| japaneast          | ✅                       | ✅                       | -                      | ✅                            |
-| koreacentral       | ✅                       | ✅                       | -                      | ✅                            |
-| northcentralus     | ✅                       | ✅                       | -                      | ✅                            |
+| francecentral      | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                       | ✅                       | ✅                       | ✅                            |
+| japaneast          | ✅                       | ✅                       | ✅                       | ✅                            |
+| koreacentral       | ✅                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                       | ✅                       | ✅                       | ✅                            |
 | norwayeast         | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                       | ✅                       | -                      | ✅                            |
-| southafricanorth   | ✅                       | ✅                       | -                      | ✅                            |
-| southcentralus     | ✅                       | ✅                       | -                      | ✅                            |
-| southeastasia      | ✅                       | ✅                       | -                      | ✅                            |
+| polandcentral      | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                       | ✅                       | ✅                       | ✅                            |
+| southeastasia      | ✅                       | ✅                       | ✅                       | ✅                            |
 | southindia         | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                       | ✅                       | -                      | ✅                            |
+| spaincentral       | ✅                       | ✅                       | ✅                       | ✅                            |
 | swedencentral      | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                       | ✅                       | -                      | ✅                            |
-| switzerlandwest    | ✅                       | ✅                       | -                      | ✅                            |
-| uaenorth           | ✅                       | ✅                       | -                      | ✅                            |
-| uksouth            | ✅                       | ✅                       | -                      | ✅                            |
+| switzerlandnorth   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | ✅                       | ✅                       | ✅                       | ✅                            |
+| uaenorth           | ✅                       | ✅                       | ✅                       | ✅                            |
+| uksouth            | ✅                       | ✅                       | ✅                       | ✅                            |
 | westeurope         | ✅                       | ✅                       | ✅                       | ✅                            |
 | westus             | ✅                       | ✅                       | ✅                       | ✅                            |
 | westus3            | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新モデルの地域サポート情報の更新"
}
```

### Explanation
このコードの変更では、Azure OpenAIに関連するグローバルなモデルプロビジョニングに関するドキュメントが改訂され、以下の主要な内容が更新されています：

1. **更新日付の変更**: ドキュメントの日付が「2025年1月15日」から「2025年2月6日」に変更され、最新の情報が反映されています。

2. **地域サポート情報の追加**: 特定の地域での`gpt-4o`および`gpt-4o-mini`モデルのサポート情報が更新され、多くの地域でサポートが追加されています。この変更により、以下の地域のモデルサポートが改善されました:
   - `brazilsouth`
   - `canadacentral`
   - `francecentral`
   - `germanywestcentral`
   - `japaneast`
   - `koreacentral`
   - `northcentralus`
   - `polandcentral`
   - `southafricanorth`
   - `southcentralus`
   - `southeastasia`
   - `spaincentral`
   - `switzerlandnorth`
   - `switzerlandwest`
   - `uaenorth`
   - `uksouth`

3. **モデルの可用性**: 各地域において、モデルの利用可否が「✅」で更新され、これによりユーザーは各地域での最新のモデルサポート状況を把握できるようになっています。

このように、ドキュメントの情報が最新かつ正確になり、ユーザーがAzure OpenAIのモデルを利用する際の地域別サポートに関する重要な情報をより簡単に参照できるようになりました。

## articles/ai-services/openai/includes/model-matrix/standard-completions.md{#item-a9c095}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,10 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/25/2024
+ms.date: 02/06/2025
 ---
 
-| **Region**   | **gpt-35-turbo-instruct**, **0914**   | **babbage-002**, **1**   | **davinci-002**, **1**   |
-|:-----------------|:-----------------------------------:|:----------------------:|:----------------------:|
-| eastus           | ✅                                | -                  | -                  |
-| northcentralus   | -                               | ✅                   | ✅                   |
-| swedencentral    | ✅                                | ✅                   | ✅                   |
+| **Region**   | **gpt-35-turbo-instruct**, **0914**   |
+|:-----------------|:-----------------------------------:|
+| eastus           | ✅                                |
+| swedencentral    | ✅                                |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準的なコンプリートモデル情報の簡素化と更新"
}
```

### Explanation
このコードの変更では、標準的なコンプリートモデルに関するドキュメントが改訂され、以下の主要な内容が更新されています：

1. **更新日付の変更**: ドキュメントの日付が「2024年10月25日」から「2025年2月6日」に変更され、最新の情報が反映されています。

2. **テーブルの簡素化**: モデルに関連する地域サポートのテーブルが簡素化され、`gpt-35-turbo-instruct`, `babbage-002`, `davinci-002`の情報が削除され、`gpt-35-turbo-instruct`専用の情報のみが残りました。これにより、情報が明確になり、ユーザーは必要な情報をより簡単に得ることができます。

3. **地域サポートの明確化**: 現在のテーブルには、`eastus`および`swedencentral`の地域にのみ、`gpt-35-turbo-instruct`モデルのサポート状況が表示されており、それぞれの地域でのモデルの利用可否が「✅」で示されています。

この変更によって、標準的なコンプリートモデルに関する情報が整理され、ユーザーにとってより理解しやすく、必要な情報へのアクセスが容易になっています。また、古い情報が削除されることで、最新の情報を中心にした明快な内容になっています。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -6,32 +6,31 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 01/23/2025
+ms.date: 02/06/2025
 ---
 
-| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   |
-|:-------------------|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:----------------------------------------:|:-------------------------------:|
-| australiaeast      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| brazilsouth        | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| canadaeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| eastus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| eastus2            | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                            |
-| francecentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| germanywestcentral | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| japaneast          | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| koreacentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| northcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| norwayeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| polandcentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| southafricanorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| southcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| southindia         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| spaincentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| swedencentral      | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                            |
-| switzerlandnorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| uaenorth           | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| uksouth            | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| westeurope         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| westus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-| westus3            | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | ✅                            |
-
+| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   |
+|:-------------------|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:-------------------------------:|
+| australiaeast      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| brazilsouth        | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| canadaeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| eastus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| eastus2            | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                                             | ✅                            |
+| francecentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| germanywestcentral | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| japaneast          | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| koreacentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| northcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| norwayeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| polandcentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| southafricanorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| southcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| southindia         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| spaincentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| swedencentral      | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                                             | ✅                            |
+| switzerlandnorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| uaenorth           | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| uksouth            | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| westeurope         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| westus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| westus3            | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準グローバルモデルのサポート地域の情報更新"
}
```

### Explanation
このコードの変更では、標準グローバルモデルに関するドキュメントが改訂され、以下の主要な内容が更新されています：

1. **更新日付の変更**: ドキュメントの日付が「2025年1月23日」から「2025年2月6日」に変更されました。これにより、情報の最新性が保証されています。

2. **モデルサポート地域情報の更新**: テーブルが再構成され、さまざまなモデル（`o3-mini`, `o1`, `gpt-4o`など）の地域サポート情報が更新されました。削除された地域情報があり、代わりに新しい地域のサポート状況が追加されています。これにより、各地域でのモデルの可用性がより明確になりました。

3. **地域におけるモデルの可用性**: 主要な地域（`australiaeast`, `brazilsouth`, `canadaeast`, `eastus`, `swedencentral`など）において、特定のモデルが利用可能であることが示されており、これによりユーザーは自身の地域における最新のモデル情報を確認しやすくなっています。この情報は、モデルの利用計画を立てる際に重要です。

この変更によって、標準グローバルモデルに関する情報が整理され、ユーザーが必要とする地域モデルサポート情報へのアクセスが容易になり、新しいモデルのリリース情報が適切にアップデートされています。

## articles/ai-services/openai/includes/model-matrix/standard-image-generation.md{#item-dd78ea}

<details>
<summary>Diff</summary>
````diff
@@ -6,11 +6,11 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 10/25/2024
+ms.date: 02/06/2025
 ---
 
-| **Region**   | **dall-e-2**, **2.0**   | **dall-e-3**, **3.0**   |
-|:-----------------|:---------------------:|:---------------------:|
-| australiaeast    | -                 | ✅                  |
-| eastus           | ✅                  | ✅                  |
-| swedencentral    | -                 | ✅                  |
\ No newline at end of file
+| **Region**   | **dall-e-3**, **3.0**   |
+|:-----------------|:---------------------:|
+| australiaeast    | ✅                  |
+| eastus           | ✅                  |
+| swedencentral    | ✅                  |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像生成モデルの地域サポート情報の更新"
}
```

### Explanation
このコードの変更では、画像生成モデルに関するドキュメントが改訂され、以下の主要な内容が更新されています：

1. **更新日付の変更**: ドキュメントの日付が「2024年10月25日」から「2025年2月6日」に更新され、最新の状態が反映されています。

2. **モデルサポートの整理**: テーブルが見直され、`dall-e-2`の情報が削除され、新たに`dall-e-3`モデルのみに焦点が当てられています。これにより、情報が簡素化され、ユーザーが必要とする重要な情報にアクセスしやすくなります。

3. **地域サポートの拡充**: `dall-e-3`モデルが、`australiaeast`, `eastus`, `swedencentral`のすべての地域で利用可能であることが示されており、各地域におけるモデルの可用性が「✅」で示されています。これにより、ユーザーは自分の地域での最新のモデル情報を確認しやすくなっています。

この変更により、画像生成モデルに関する情報が整理され、ユーザーが利用可能な地域やモデルについての理解が深まることが期待されます。また、古い情報が除去されることで、最新の情報に基づいた判断を下せるようになります。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,29 +5,29 @@ description: Quota and limits for Azure OpenAI by region.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/16/2024
+ms.date: 02/06/2025
 ---
 
 
-| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **dall-e-2**, **2.0**   | **dall-e-3**, **3.0**   | **babbage-002**, **1**   | **davinci-002**, **1**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
-|:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:---------------------:|:----------------------:|:----------------------:|:----------------:|:-------------------:|:--------------------:|
-| australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | ✅                  | -                  | -                  | -            | -               | -                |
-| brazilsouth      | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| canadaeast       | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | ✅                  | -                  | -                  | -            | -               | -                |
-| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| francecentral    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                       | -                      | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
-| norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| polandcentral    | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -                 | -                  | -                  | -            | -               | -                |
-| southafricanorth | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | -                             | -                             | ✅                              | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| southindia       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | -                      | ✅                       | ✅                       | -                      | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | -                 | ✅                  | ✅                   | ✅                   | ✅             | ✅                | ✅                 |
-| switzerlandnorth | -                          | -                       | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| uaenorth         | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | ✅                 |
-| westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | ✅                              | -                             | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
-| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -                 | -                  | -                  | -            | -               | -                |
+| **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **dall-e-3**, **3.0**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
+|:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:----------------:|:-------------------:|:--------------------:|
+| australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | ✅                  | -            | -               | -                |
+| brazilsouth      | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -            | -               | -                |
+| canadaeast       | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| eastus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | ✅                       | -                      | ✅                       | ✅                           | ✅                                | ✅                              | ✅                              | ✅                              | ✅                              | ✅                  | -            | -               | -                |
+| eastus2          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| francecentral    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | -                         | -                           | ✅                    | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| japaneast        | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | ✅                          | -                           | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| northcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | -                       | ✅                        | -                         | ✅                            | -                   | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | -                             | -                             | -                             | ✅                              | -                 | ✅             | ✅                | ✅                 |
+| norwayeast       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| polandcentral    | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | -                             | -                 | -            | -               | -                |
+| southafricanorth | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -            | -               | -                |
+| southcentralus   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | -                       | ✅                        | -                         | ✅                            | -                   | ✅                       | -                      | -                      | ✅                       | -                          | -                               | -                             | -                             | ✅                              | ✅                              | -                 | -            | -               | -                |
+| southindia       | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | -                       | -                         | -                           | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| swedencentral    | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                          | ✅                            | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | ✅                                | -                             | ✅                              | -                             | ✅                              | ✅                  | ✅             | ✅                | ✅                 |
+| switzerlandnorth | -                          | -                       | -                      | -                      | -                           | ✅                | -                       | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | -                      | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| uaenorth         | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | -                      | -                      | -                      | -                      | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
+| westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          | -                               | -                             | -                             | -                             | ✅                              | -                 | -            | -               | ✅                 |
+| westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          | -                               | ✅                              | -                             | -                             | ✅                              | -                 | -            | -               | -                |
+| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          | -                               | -                             | ✅                              | -                             | ✅                              | -                 | -            | -               | -                |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準モデルの地域サポート情報の更新"
}
```

### Explanation
このコード変更では、標準モデルに関するドキュメントが改訂され、以下の主な内容が更新されています：

1. **更新日付の変更**: ドキュメントの日付が「2024年12月16日」から「2025年2月6日」に変更され、内容が最新の情報に基づいていることが確認できます。

2. **モデルサポートの整理**: モデルのサポート情報が整理され、特に`dall-e-3`が新たに追加されました。これにより、ユーザーは最新の画像生成モデルの情報にアクセスできます。

3. **地域サポートの拡充**: 各モデルに対する地域サポートの可用性が見直され、一部の地域での新たなモデル利用状況が反映されています。例えば、`dall-e-3`モデルが複数の地域で利用可能であることが示されており、地域ごとのサポート状況が「✅」で示されています。

4. **表の構成の変更**: ドキュメント内のテーブルが再構成され、モデルと地域に関する情報がより明確に整理されています。これにより、ユーザーが必要な情報を迅速に見つけやすくなりました。

この変更によって、標準モデルの地域サポート情報が更新され、最新のモデルとその可用性がユーザーに提供されるようになりました。このような情報の整理は、ユーザーが自分のニーズに合ったモデルを選択する際に非常に重要です。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 | Feature | Azure OpenAI |
 | --- | --- |
 | Models available | [**o3-mini & o1**](./how-to/reasoning.md) - (Limited Access - [**Request Access**](https://aka.ms/OAI/o1access))<br>[**o1-mini**](./how-to/reasoning.md)<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
-| Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613) <br> `babbage-002` <br> `davinci-002`.|
+| Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613).|
 | Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
 | Managed Identity| Yes, via Microsoft Entra ID | 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングモデル情報の更新"
}
```

### Explanation
このコード変更では、Azure OpenAIサービスに関するドキュメントの一部が改訂され、具体的にはファインチューニングに関するモデルの情報が更新されています。以下の点が変更されました：

1. **ファインチューニングモデルの削減**: ドキュメント内のファインチューニング対応モデルのリストから、`babbage-002`と`davinci-002`が削除されました。この結果、現在ファインチューニングに対応しているモデルは`GPT-4o-mini`、`GPT-4`、および`GPT-3.5-Turbo`（0613）のみとなります。

2. **内容の明確化**: モデルの情報が簡素化され、現在利用可能なファインチューニングモデルが明確に示されることで、ユーザーが重要な情報により迅速にアクセスできるようになっています。

この変更により、ユーザーは最新のファインチューニングに対応したモデルを理解し、利用可能なオプションについての把握が容易になります。また、不要な情報が削除されることで、ドキュメント全体がよりクリーンで使いやすくなっています。


