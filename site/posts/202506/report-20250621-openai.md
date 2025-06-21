---
date: '2025-06-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fc0b900...MicrosoftDocs:fb526ea
summary: この記事では、Azure OpenAIサービスにおける文書の最新情報を含むいくつかの重要な更新についてまとめています。主なポイントとして、新モデルの追加、レスポンスAPIの大幅な改訂、モデルのクォータや制限に関する整理、さらに新しい健康フィルター設定やSMS通知機能の導入が挙げられます。これにより、ユーザーはサービスの利用をより効率的に行えるようになり、特に最近のモデルや地域拡大に関する明確な情報が提供されています。全体的に、これらの更新はAIサービスの利用における柔軟性と信頼性を向上させる狙いがあります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fc0b900...MicrosoftDocs:fb526ea){target="_blank"}

<format>
# ハイライト
この記事ではAzure OpenAIサービスにおけるいくつかの文書更新を詳しく説明しています。主なポイントは、モデルの引退、ファインチューニング、レスポンスAPI、バッチ制限、モデルのクォータと制限に関する情報が整理され、新モデルの追加も行われました。

## 新機能
- `gpt-4.1-2025-04-14`および`gpt-4.1-mini-2025-04-14`モデルが直接的好み最適化をサポート。
- 新しい健康フィルター設定、SMS通知の設定が導入。

## 破壊的変更
- レスポンスAPI文書が大規模に改訂され、新機能および非対応機能についての記載が変わりました。

## その他の更新
- バッチ制限表に新しいモデルが追加。
- モデルのクォータ情報が更新し、表が見やすく整理。
- モデル名の表記修正で一部ドキュメントが精度向上。

# インサイト
このコード変更は、Azure OpenAIサービスのドキュメントを全般的に最新の情報でアップデートし、利用者がより的確にサービスを利用できるように設計されています。

## 詳細な文書の更新
最新モデルに対するサポートを明確にすることで、ユーザーは利用可能なファインチューニングモデルについての理解を深めることができます。新しい健康通知のフィルター設定とSMS通知の導入は、クライアントにとって新たなカスタマイズの可能性をもたらします。これにより、モデルの供用停止が近づいた場合、利用者への確実な情報伝達が保証されます。

## レスポンスAPIの改善と地域拡大
レスポンスAPIに関連する文書の大幅な更新により、情報の整理が行われ、特に新興地域である「polandcentral」と「switzerlandnorth」の追加は、ユーザーの地域サービスへのアクセスを広げる動きといえます。また、非対応の機能への明確な言及により、期待されるAPIの範囲がはっきりしました。

## モデル情報のクリアな整理
クォータと制限に関連した情報更新により、利用者は各モデルに対するリソースの割当てについて具体的な理解を持つことができるようになりました。これにより、予想されるトラフィックやリソース使用に基づいた計画を立てやすくなり、運用効率が向上します。

全体として、これらの文書改訂はユーザーがサービスをより効率的に利用し、発生した変化や新機能に迅速に対応できる手助けをしています。特に、新モデルの追加や既存機能の見直しは、AIサービスを利用する際の柔軟性と信頼性を高めるものとなっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルの引退に関する情報の追加 | modified | 10 | 0 | 10 | 
| [fine-tuning-direct-preference-optimization.md](#item-384724) | minor update | 直接的好み最適化モデルのサポートに関する情報更新 | modified | 2 | 2 | 4 | 
| [responses.md](#item-b9757d) | breaking change | レスポンスAPIに関する文書の大規模な改訂 | modified | 8 | 56 | 64 | 
| [global-batch-limits.md](#item-73207b) | minor update | バッチ制限に関するモデルの追加 | modified | 6 | 0 | 6 | 
| [quotas-limits.md](#item-06c6f9) | minor update | モデルのクォータと制限の更新 | modified | 16 | 12 | 28 | 
| [whats-new.md](#item-53303b) | minor update | モデル名の表記修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -41,6 +41,16 @@ Azure OpenAI notifies customers via two methods:
 - **Azure Resource Health** - Anyone with reader permissions or above can see Azure health alerts, as well as configure personalized alerts via email, SMS, etc. See [Create Service Health Alerts](/azure/service-health/alerts-activity-log-service-notifications-portal)
 - **Email** - email notifications are automatically sent to subscription owners. Any individual with reader permissions may however configure their own alerts by following the guidance above.
 
+**Azure Service Health filter configuration**:
+
+**Services** = `azure OpenAI service` (Casing reflects current UX experience).
+
+**Event types**
+    - `Health advisories = Upgrade, Deprecation, & Retirement Notifications`
+    - `Service issue = Outages` (Recommended only if you wish to be notified of outages)
+
+If you wish to receive SMS text-based alerts rather than just e-mails, you will need to select **Create action group** and under **Notification type**, select **Email/SMS message/Push/Voice** and then configure your phone number.
+
 ## Model availability
 
 1. At least one year of model availability for GA models after the release date of a model in at least one region worldwide
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの引退に関する情報の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するモデルの引退に関する文書に小規模な更新を加えたものです。具体的には、Azure OpenAIが顧客に通知を行う方法についてのセクションに新たに数項目が追加され、Azureサービス健康フィルターの設定に関する具体的な指示が記載されています。

変更内容は以下の通りです：
- Azureサービステンプレートに基づく新しい健康フィルター構成が導入され、サービス名やイベントタイプについての詳細が加わりました。
- 特に、ユーザーがSMS通知を受け取るための設定手順も明記され、通知のカスタマイズがより具体的に説明されています。

これにより、ユーザーはモデルの利用状況と重要な通知について、より効果的に管理できるようになります。この更新は、ドキュメンテーションの明確さを向上させ、利用者に役立つ情報を提供することを目指しています。

## articles/ai-services/openai/how-to/fine-tuning-direct-preference-optimization.md{#item-384724}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ Training datasets must be in `jsonl` format:
 
 ## Direct preference optimization model support
 
-- `gpt-4o-2024-08-06` supports direct preference optimization in its respective fine-tuning regions. Latest region availability is updated in the [models page](../concepts/models.md#fine-tuning-models)
+- `gpt-4o-2024-08-06`,`gpt-4.1-2025-04-14`,`gpt-4.1-mini-2025-04-14`  supports direct preference optimization in its respective fine-tuning regions. Latest region availability is updated in the [models page](../concepts/models.md#fine-tuning-models)
 
 Users can use preference fine tuning with base models as well as models that have already been fine-tuned using supervised fine-tuning as long as they are of a supported model/version.
 
@@ -70,4 +70,4 @@ Users can use preference fine tuning with base models as well as models that hav
 
 - Explore the fine-tuning capabilities in the [Azure OpenAI fine-tuning tutorial](../tutorials/fine-tune.md).
 - Review fine-tuning [model regional availability](../concepts/models.md#fine-tuning-models)
-- Learn more about [Azure OpenAI quotas](../quotas-limits.md)
\ No newline at end of file
+- Learn more about [Azure OpenAI quotas](../quotas-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "直接的好み最適化モデルのサポートに関する情報更新"
}
```

### Explanation
この修正は、Azure OpenAIサービスにおける「直接的好み最適化」に関する文書を小規模に整備したものです。具体的な変更点は以下の通りです：

- `gpt-4o-2024-08-06`モデルだけでなく、新たに`gpt-4.1-2025-04-14`および`gpt-4.1-mini-2025-04-14`モデルも直接的好み最適化をサポートすることが記載され、サポートされているモデルの範囲が広がりました。
- 各モデルのファインチューニング地域における最新の可用性情報については、引き続き[モデルページ](../concepts/models.md#fine-tuning-models)で更新されることが強調されています。
- また、文書の結びにはAzure OpenAIのクォータに関するリンクが整理されています。

これらの更新により、ユーザーは利用可能なモデルとそのサポート状況についての理解を深めることができ、ファインチューニングに関する情報をより効果的に活用できるようになります。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's new stateful Responses API.
 author: mrbullwinkle
 ms.author: mbullwin
 manager: nitinme
-ms.date: 05/25/2025
+ms.date: 06/20/2025
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom:
@@ -33,8 +33,10 @@ The responses API is currently available in the following regions:
 - francecentral
 - japaneast
 - norwayeast
+- polandcentral
 - southindia
 - swedencentral
+- switzerlandnorth
 - uaenorth
 - uksouth
 - westus
@@ -58,9 +60,12 @@ Not every model is available in the regions supported by the responses API. Chec
 > Not currently supported:
 > - The web search tool
 > - Fine-tuned models
-> - Image generation via streaming. Coming soon.
+> - Image generation using multi-turn editing and streaming - coming soon
 > - Images can't be uploaded as a file and then referenced as input. Coming soon.
-> - There's a known issue with performance when background mode is used with streaming. The issue is expected to be resolved soon. 
+>
+> There's a known issue with the following:
+> - PDF as an input file is not yet supported.
+> - Performance when background mode is used with streaming. The issue is expected to be resolved soon.
 
 ### Reference documentation
 
@@ -1071,7 +1076,6 @@ The Responses API enables image generation as part of conversations and multi-st
 
 Compared to the standalone Image API, the Responses API offers several advantages:
 
-* **Multi-turn editing**: Iteratively refine and edit images using natural language prompts.
 * **Streaming**: Display partial image outputs during generation to improve perceived latency.
 * **Flexible inputs**: Accept image File IDs as inputs, in addition to raw image bytes.
 
@@ -1081,7 +1085,6 @@ Compared to the standalone Image API, the Responses API offers several advantage
 Use the Responses API if you want to:
 
 * Build conversational image experiences with GPT Image.
-* Enable iterative image editing through multi-turn prompts.
 * Stream partial image results during generation for a smoother user experience.
 
 Generate an image
@@ -1121,57 +1124,6 @@ if image_data:
         f.write(base64.b64decode(image_base64))
 ```
 
-You can perform multi-turn image generation by using the output of image generation in subsequent calls or just using the `1previous_response_id`.
-
-```python
-from openai import AzureOpenAI
-from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-
-token_provider = get_bearer_token_provider(
-    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
-)
-
-client = AzureOpenAI(  
-  base_url = "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  
-  azure_ad_token_provider=token_provider,
-  api_version="preview",
-  default_headers={"x-ms-oai-image-generation-deployment":"YOUR-GPT-IMAGE1-DEPLOYMENT-NAME"}
-)
-
-image_data = [
-    output.result
-    for output in response.output
-    if output.type == "image_generation_call"
-]
-
-if image_data:
-    image_base64 = image_data[0]
-
-    with open("cat_and_otter.png", "wb") as f:
-        f.write(base64.b64decode(image_base64))
-
-
-# Follow up
-
-response_followup = client.responses.create(
-    model="gpt-4.1-mini",
-    previous_response_id=response.id,
-    input="Now make it look realistic",
-    tools=[{"type": "image_generation"}],
-)
-
-image_data_followup = [
-    output.result
-    for output in response_followup.output
-    if output.type == "image_generation_call"
-]
-
-if image_data_followup:
-    image_base64 = image_data_followup[0]
-    with open("cat_and_otter_realistic.png", "wb") as f:
-        f.write(base64.b64decode(image_base64))
-```
-
 ### Streaming
 
 You can stream partial images using Responses API. The `partial_images` can be used to receive 1-3 partial images
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "レスポンスAPIに関する文書の大規模な改訂"
}
```

### Explanation
この変更は、Azure OpenAIのレスポンスAPIに関する文書を大幅に改訂したもので、主に情報の整理および更新が行われています。以下は変更の概要です：

- 文書の冒頭部分で、日付が2025年5月25日から2025年6月20日に変更されています。
- レスポンスAPIが利用可能な地域に新たに「polandcentral」と「switzerlandnorth」が追加され、地域の範囲が拡大しました。
- 非対応の機能についての説明も更新され、画像生成に関する詳細が変更されています。特に、マルチターン編集とストリーミングを使用する画像生成についても言及されています。
- 文書内の多くの古いコードスニペットや情報が削除され、新たな構造に整理されました。特に、マルチターン画像生成に関するコードが完全に削除され、その内容が簡潔に説明されています。

このような大規模な改訂により、利用者はレスポンスAPIの機能や制限について最新の情報をより理解しやすくなり、利用方法に関する指針がより明確になります。更新された文書は、ユーザーがAPIを効果的に利用するための重要な情報を提供します。

## articles/ai-services/openai/includes/global-batch-limits.md{#item-73207b}

<details>
<summary>Diff</summary>
````diff
@@ -24,19 +24,25 @@ The table shows the batch quota limit. Quota values for global batch are represe
 
 |Model|Enterprise agreement|Default| Monthly credit card based subscriptions | MSDN subscriptions | Azure for Students, Free Trials |
 |---|---|---|---|---|---|
+| `gpt-4.1`| 5 B | 200 M | 50 M | 90 K | N/A |
+| `gpt-4.1 mini` | 15B | 1B | 50M | 90k | N/A |
+| `gpt-4.1-nano` | 15 B | 1 B | 50 M | 90 K | N/A |
 | `gpt-4o` | 5 B | 200 M | 50 M | 90 K | N/A|
 | `gpt-4o-mini` | 15 B | 1 B | 50 M | 90 K | N/A |
 | `gpt-4-turbo` | 300 M | 80 M | 40 M | 90 K | N/A |
 | `gpt-4` | 150 M | 30 M | 5 M | 100 K | N/A |
 | `gpt-35-turbo` | 10 B | 1 B | 100 M | 2 M | 50 K |
 | `o3-mini`| 15 B | 1 B | 50 M | 90 K | N/A |
+| `o4-mini` | 15 B | 1 B | 50 M | 90 K | N/A |
 
 B = billion | M = million | K = thousand
 
 ### Data zone batch
 
 |Model|Enterprise agreement|Default| Monthly credit card based subscriptions | MSDN subscriptions | Azure for Students, Free Trials |
 |---|---|---|---|---|---|
+| `gpt-4.1` | 500 M | 30 M | 30 M | 90 K | N/A|
+| `gpt-4.1-mini` | 1.5 B | 100 M | 50 M | 90 K | N/A |
 | `gpt-4o` | 500 M | 30 M | 30 M | 90 K | N/A|
 | `gpt-4o-mini` | 1.5 B | 100 M | 50 M | 90 K | N/A |
 | `o3-mini` | 1.5 B | 100 M | 50 M | 90 K | N/A |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ制限に関するモデルの追加"
}
```

### Explanation
この修正は、Azure OpenAIサービスにおけるバッチ制限に関する情報を更新し、いくつかのモデルを新たに追加したものです。具体的には、以下の変更が行われています：

- **グローバルバッチ制限**の表に、`gpt-4.1`、`gpt-4.1 mini`、`gpt-4.1-nano`、および`o4-mini`モデルが追加されました。これにより、これらのモデルに対するバッチ制限が明確になり、使用可能なクォータが示されています。
- 各モデルのエンタープライズ契約、デフォルト、月額クレジットカードベースのサブスクリプション、MSDNサブスクリプション、Azure for Studentsおよび無料トライアルでのバッチ制限数値が提供されています。

これらの更新により、ユーザーは異なるプランにおける新モデルのバッチ制限を理解しやすくなり、リソース使用計画をより適切に行えるようになります。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -126,18 +126,22 @@ The following sections provide you with a quick guide to the default quotas and
 
 ### o-series global standard
 
-| Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
-|---|---|:---:|:---:|
-| `o4-mini` | Enterprise agreement | 10 M | 10 K |
-| `o3` | Enterprise agreement | 10 M | 10 K |
-| `o3-mini` | Enterprise agreement | 50 M | 5 K |
-| `o1` & `o1-preview` | Enterprise agreement | 30 M | 5 K |
-| `o1-mini`| Enterprise agreement | 50 M | 5 K |
-| `o4-mini` | Default | 1 M | 1 K  |
-| `o3` | Default | 1 M | 1 K |
-| `o3-mini` | Default | 5 M | 500 |
-| `o1` & `o1-preview` | Default | 3 M | 500 |
-| `o1-mini`| Default | 5 M | 500 |
+| Model              |Tier                    | Quota Limit in tokens per minute (TPM) | Requests per minute |
+|--------------------|------------------------|:--------------------------------------:|:---:  |
+| `codex-mini`       | Enterprise agreement   | 10 M                                   | 10 K  |
+| `o3-pro`           | Enterprise agreement   | 16 M                                   | 1.6 K |
+| `o4-mini`          | Enterprise agreement   | 10 M                                   | 10 K  |
+| `o3`               | Enterprise agreement   | 10 M                                   | 10 K  |
+| `o3-mini`          | Enterprise agreement   | 50 M                                   | 5 K   |
+| `o1` & `o1-preview`| Enterprise agreement   | 30 M                                   | 5 K   |
+| `o1-mini`          | Enterprise agreement   | 50 M                                   | 5 K   |
+| `codex-mini`       | Default                | 1 M                                    | 1 K   |
+| `o3-pro`           | Default                | 1.6 M                                  | 160   |
+| `o4-mini`          | Default                | 1 M                                    | 1 K   |
+| `o3`               | Default                | 1 M                                    | 1 K   |
+| `o3-mini`          | Default                | 5 M                                    | 500   |
+| `o1` & `o1-preview`| Default                | 3 M                                    | 500   |
+| `o1-mini`          | Default                | 5 M                                    | 500   |
 
 ### o-series data zone standard
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのクォータと制限の更新"
}
```

### Explanation
この修正では、Azure OpenAIサービスにおけるモデルのクォータおよび制限に関する情報が更新されています。具体的には、以下の変更が行われています：

- **新モデルの追加**: `codex-mini`および`o3-pro`モデルがエンタープライズ契約とデフォルトプランの両方に追加され、それぞれのトークン毎分（TPM）とリクエスト毎分の制限が明示されています。
- **表の形式の改善**: モデル名、ティア、クォータ制限、リクエスト制限を含む表が整形され、情報をより見やすく整理しました。
- **従来のモデルの情報更新**: 既存のモデル（`o4-mini`、`o3`、`o3-mini`、`o1`、`o1-preview`、`o1-mini`）のクォータとリクエスト制限の情報も含まれていますが、これも新たに整理されています。

これらの更新により、ユーザーは各モデルに対する具体的なクォータ制限を把握しやすくなり、リソースの使用計画をより効果的に行えるようになります。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ This article provides a summary of the latest releases and major documentation u
 
 ### codex-mini & o3-pro models released
 
-- `codex-mini and `o3-pro` are now available. To learn more, see the [getting started with reasoning models page](./how-to/reasoning.md)
+- `codex-mini` and `o3-pro` are now available. To learn more, see the [getting started with reasoning models page](./how-to/reasoning.md)
 
 ## May 2025
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル名の表記修正"
}
```

### Explanation
この修正では、Azure OpenAIサービスに関する「新機能」ページで、`codex-mini`および`o3-pro`モデルの表記に関する軽微な修正が行われました。具体的には、以下の変更が行われています：

- モデル名の表記が修正され、`codex-mini`と`o3-pro`の間にバッククォートが適切に追加されました。この変更により、モデル名が正確に表示され、より明確な情報提供が実現されています。
- これに伴い、該当する文の整合性も保たれ、ユーザーが新しいモデルに関する情報を適切に理解できるようになりました。

このような修正により、ドキュメントの精度が向上し、ユーザーが情報をスムーズに取得できるよう改善されています。


