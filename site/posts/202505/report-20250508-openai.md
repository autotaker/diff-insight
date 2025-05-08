---
date: '2025-05-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:768f68b...MicrosoftDocs:8ab07ce
summary: Azure OpenAIサービスのドキュメントに小規模な更新があり、情報の正確性と利用者の利便性が向上しました。主な変更点として、新しいモデルの追加やモデルマトリックスの更新、オブジェクト名の変更があり、特に「content_filter_result」が「content_filter_results」に改名されました。また、モデルリタイアメントに関する情報が更新され、利用者に事前通知が行われるようになっています。これにより、ユーザーはモデルの移行やサービスの変更を適切なタイミングで行うことができ、地域ごとの利用可能性も明確に示されるため、より良いユーザー体験が期待されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:768f68b...MicrosoftDocs:8ab07ce){target="_blank"}

<format>
# Highlights
Azure OpenAIサービスのドキュメントにおけるいくつかの小規模な更新が行われ、情報の正確性と利用者の利便性が向上しました。特に、オブジェクト名の変更やモデルマトリックスの更新、新しいモデルの追加が中心となります。

## New features
- モデルリストやモデルマトリックスに新しいモデルが追加され、地域ごとの利用可能性が詳細に示されました。
- プロビジョニングされたスループット仕様およびエラーレスポンスフィールド名の修正。

## Breaking changes
- オブジェクト名の「content_filter_result」から「content_filter_results」に変更され、影響範囲があるコードは適切に調整する必要があります。

## Other updates
- モデルリタイアメントに関する通知に関する情報が更新され、利用者により明確な予測可能性が提供されるようになりました。
- モデルマトリックスにおけるバージョン情報や地域情報の更新により、ドキュメントの整合性が向上します。

# Insights
この一連の更新では、Azure OpenAIの様々な機能に関するドキュメントが、最新の技術的進化に伴って改訂されました。まず、`content_filter_result`の変更は、一貫性を保ちつつ、結果の複数性を反映するためです。こうした調整は、エラーメッセージやログの解釈を容易にし、デバッグを効率化します。

次に、モデルリストやリタイアメント情報の更新で、利用者はサービスのサポート終了に関して事前通知を受けられるようになりました。これにより、ユーザーは適切なタイミングでモデルを移行したりサービスを変更したりすることができます。

加えて、地域ごとの情報が見直されたことにより、利用者は利用可能なモデルの詳細な内訳を理解しやすくなりました。特に、新規モデルの追加は選択肢を拡充し、ユーザーのニーズに合ったモデル選択を可能にします。最終的に、こうしたドキュメンテーションの更新は、サービスの透明性を向上させ、より良いユーザー体験を提供するための重要な改訂となっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-filter.md](#item-dfc7e7) | minor update | コンテンツフィルタの結果オブジェクト名の修正 | modified | 7 | 7 | 14 | 
| [model-retirements.md](#item-03fc2e) | minor update | モデルリタイアメントに関する通知の追加 | modified | 3 | 3 | 6 | 
| [models.md](#item-db2c37) | minor update | モデルリストの地域情報の整理 | modified | 8 | 8 | 16 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョニングされたスループットの仕様更新 | modified | 8 | 8 | 16 | 
| [use-blocklists.md](#item-e99db7) | minor update | ブロックリストのレスポンスフィールドの修正 | modified | 1 | 1 | 2 | 
| [python.md](#item-9cca6c) | minor update | Pythonコード内のレスポンスフィールドの修正 | modified | 2 | 2 | 4 | 
| [datazone-provisioned-managed.md](#item-ae7f5b) | minor update | モデルマトリックスの更新 | modified | 16 | 15 | 31 | 
| [datazone-standard.md](#item-188333) | minor update | モデルマトリックスのバージョン更新 | modified | 15 | 15 | 30 | 
| [global-batch.md](#item-929e6a) | minor update | グローバルバッチモデルマトリックスの更新 | modified | 23 | 23 | 46 | 
| [provisioned-global.md](#item-340884) | minor update | プロビジョニング済みモデルマトリックスの更新 | modified | 28 | 28 | 56 | 
| [provisioned-models.md](#item-8ee639) | minor update | プロビジョニングモデルマトリックスの更新 | modified | 29 | 28 | 57 | 
| [standard-global.md](#item-17a84b) | minor update | 標準モデルマトリックスの更新 | modified | 6 | 5 | 11 | 


# Modified Contents
## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -275,7 +275,7 @@ The table below outlines the various ways content filtering can appear:
 
 **HTTP Response Code** | **Response behavior**
 |------------------------|----------------------|
-| 200 | If the content filtering system is down or otherwise unable to complete the operation in time, your request will still complete without content filtering. You can determine that the filtering wasn't applied by looking for an error message in the `content_filter_result` object.|
+| 200 | If the content filtering system is down or otherwise unable to complete the operation in time, your request will still complete without content filtering. You can determine that the filtering wasn't applied by looking for an error message in the `content_filter_results` object.|
 
 **Example request payload:**
 
@@ -301,7 +301,7 @@ The table below outlines the various ways content filtering can appear:
             "index": 0,
             "finish_reason": "length",
             "logprobs": null,
-            "content_filter_result": {
+            "content_filter_results": {
                 "error": {
                     "code": "content_filter_error",
                     "message": "The contents are not filtered"
@@ -597,12 +597,12 @@ try:
 
 except openai.error.InvalidRequestError as e:
     if e.error.code == "content_filter" and e.error.innererror:
-        content_filter_result = e.error.innererror.content_filter_result
+        content_filter_results = e.error.innererror.content_filter_result
         # print the formatted JSON
-        print(content_filter_result)
+        print(content_filter_results)
 
         # or access the individual categories and details
-        for category, details in content_filter_result.items():
+        for category, details in content_filter_results.items():
             print(f"{category}:\n filtered={details['filtered']}\n severity={details['severity']}")
 
 ```
@@ -765,7 +765,7 @@ Blocks completion content when ungrounded completion content was detected.
         "status": 400,
         "innererror": {
             "code": "ResponsibleAIPolicyViolation",
-            "content_filter_result": {
+            "content_filter_results": {
                 "hate": {
                     "filtered": true,
                     "severity": "high"
@@ -1040,7 +1040,7 @@ As part of your application design, consider the following best practices to del
 
 - Decide how you want to handle scenarios where your users send prompts containing content that is classified at a filtered category and severity level or otherwise misuse your application.
 - Check the `finish_reason` to see if a completion is filtered.
-- Check that there's no error object in the `content_filter_result` (indicating that content filters didn't run).
+- Check that there's no error object in the `content_filter_results` (indicating that content filters didn't run).
 - If you're using the protected material code model in annotate mode, display the citation URL when you're displaying the code in your application.
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタの結果オブジェクト名の修正"
}
```

### Explanation
この修正内容は、コンテンツフィルタリングに関するドキュメンテーションの一部であり、特にオブジェクト名の変更に関するものです。具体的には、`content_filter_result` というオブジェクト名が `content_filter_results` に変更されました。この変更は、フィルタリングの結果をより正確に反映させるためのものです。

ドキュメントで明示されたように、この修正は複数の場所で行われており、HTTPレスポンスコードの説明やエラーハンドリングのセクションで目立つ修正がなされています。これにより、ユーザーはフィルタリングの結果にアクセスする際、正確なオブジェクト名を使用することが求められるようになります。さらに、より良いエラーハンドリングを提供することが期待され、この点も改善されています。

総じて、この修正はシステムの一貫性を高め、開発者がコンテンツフィルタリング機能をより理解しやすくするための重要な更新です。

## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ Azure OpenAI notifies customers of active Azure OpenAI Service deployments for m
 2. At least 60 days notice before model retirement for Generally Available (GA) models.
 3. At least 30 days notice before preview model version upgrades.  
 
-Retirements are done on a rolling basis, region by region.
+Retirements are done on a rolling basis, region by region. Notifications are sent from an unmonitored mailbox, `azure-noreply@microsoft.com`.
 
 ## Model availability
 
@@ -110,8 +110,8 @@ These models are currently available for use in Azure OpenAI Service.
 | `gpt-4.1-nano`            | 2025-04-14      | No earlier than April 11, 2026     |                                      |
 | `gpt-4o`                  | 2024-05-13      | No earlier than June 30, 2025      | `gpt-4.1` version: `2025-04-14`      |
 | `gpt-4o`                  | 2024-08-06      | No earlier than August 6, 2025     | `gpt-4.1` version: `2025-04-14`      |
-| `gpt-4o`                  | 2024-11-20      | No earlier than January 30, 2026   | `gpt-4.1` version: `2025-04-14`      |
-| `gpt-4o-mini`             | 2024-07-18      | August 16, 2025                    |                                      |
+| `gpt-4o`                  | 2024-11-20      | No earlier than March 1, 2026   | `gpt-4.1` version: `2025-04-14`      |
+| `gpt-4o-mini`             | 2024-07-18      | August 16, 2025                    | `gpt-4.1-mini` version: `2025-04-14` |
 | `gpt-3.5-turbo-instruct`  | 0914            | No earlier than May 31, 2025       |                                      |
 | `gpt-image-1`             | 2025-04-15      | No earlier than August 01, 2025    |                                      |
 | `o1-preview`              | 2024-09-12      | May 29, 2025                       | `o1`                                 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルリタイアメントに関する通知の追加"
}
```

### Explanation
この修正は、Azure OpenAIサービスにおけるモデルリタイアメントの通知手順についての情報を更新したものです。具体的には、モデルがリタイアされる際に顧客に通知が行われることに関する詳細が追加されました。変更内容はいくつかの文の追加および修正に関連しており、リタイアメントの通知がどのように行われるかを明確にしています。

修正された部分では、リタイアメントが地域ごとに段階的に実施されることに加え、通知が「azure-noreply@microsoft.com」という監視されていないメールボックスから送信されることが明記されています。これにより、ユーザーは通知の発信元を正しく認識することができるようになります。

このような変更は、利用者にとって非常に重要であり、モデルリタイアメントのスケジュールを理解する助けとなります。ドキュメントの透明性を向上させ、顧客が事前に予測できるよう情報を提供することが目的とされています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 04/23/2025
+ms.date: 05/07/2025
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -35,9 +35,9 @@ Azure OpenAI Service is powered by a diverse set of models with different capabi
 
 | Model | Region |
 |---|---|
-| `gpt-4.1` (2025-04-14) | East US2 (Global Standard), Sweden Central (Global Standard) |
-| `gpt-4.1-nano` (2025-04-14) | East US2 (Global Standard), Sweden Central (Global Standard)|
-| `gpt-4.1-mini` (2025-04-14) | East US2 (Global Standard), Sweden Central (Global Standard)|
+| `gpt-4.1` (2025-04-14) |  See the [models table](#model-summary-table-and-region-availability). |
+| `gpt-4.1-nano` (2025-04-14) |  See the [models table](#model-summary-table-and-region-availability).|
+| `gpt-4.1-mini` (2025-04-14) |  See the [models table](#model-summary-table-and-region-availability).|
 
 ### Capabilities
 
@@ -67,7 +67,7 @@ Once access has been granted, you will need to create a deployment for the model
 
 | Model | Region |
 |---|---|
-| `computer-use-preview` | East US 2 (Global Standard) <br> South India (Global Standard) <br> Sweden Central (Global Standard) |
+| `computer-use-preview` |  See the [models table](#model-summary-table-and-region-availability). |
 
 ### Capabilities
 
@@ -82,7 +82,7 @@ Once access has been granted, you will need to create a deployment for the model
 
 | Model | Region |
 |---|---|
-| `gpt-4.5-preview` | East US 2 (Global Standard) <br> Sweden Central (Global Standard) |
+| `gpt-4.5-preview` |  See the [models table](#model-summary-table-and-region-availability).|
 
 ### Capabilities
 
@@ -114,8 +114,8 @@ To learn more about the advanced `o-series` models see, [getting started with re
 
 | Model | Region |
 |---|---|
-|`o4-mini`|  East US2 (Global Standard) <br> Sweden Central (Global Standard)  |
-| `o3` |  East US2 (Global Standard) <br> Sweden Central (Global Standard)  |
+|`o4-mini`|   See the [models table](#model-summary-table-and-region-availability).  |
+| `o3` |   See the [models table](#model-summary-table-and-region-availability).  |
 |`o3-mini` | See the [models table](#model-summary-table-and-region-availability). |
 |`o1` | See the [models table](#model-summary-table-and-region-availability). |
 | `o1-preview` | See the [models table](#model-summary-table-and-region-availability). This model is only available for customers who were granted access as part of the original limited access |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルリストの地域情報の整理"
}
```

### Explanation
この修正は、Azure OpenAIサービスにおけるモデルの情報を整理したものです。具体的には、各モデルの利用可能な地域を示す部分において、従来の地域名が削除され、代わりに「モデルの概要表」を参照するように変更されました。これにより、地域情報が一元化され、ドキュメンテーションの他の部分との整合性が保たれることになります。

修正内容には、以下のような主な変更が含まれます：
- 各モデルの地域情報を具体的な地域名から、モデルの概要表へのリンクに置き換え。
- 日付が「04/23/2025」から「05/07/2025」へと更新。

この改訂により、ユーザーは地域に関する最新の情報を簡単に確認できるようになり、実際の利用可能な地域を把握しやすくなります。全体として、ドキュメントの可読性と機能的な価値が向上しています。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -81,15 +81,15 @@ The amount of throughput (measured in tokens per minute or TPM) a deployment get
 
 For example, for `gpt-4.1:2025-04-14`, 1 output token counts as 4 input tokens towards your utilization limit which matches the [pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). Older models use a different ratio and for a deeper understanding on how different ratios of input and output tokens impact the throughput your workload needs, see the [Azure OpenAI capacity calculator](https://ai.azure.com/resource/calculator).
 
+|Topic| **gpt-4.1** | **gpt-4.1-mini** | **o3-mini** | **o1** | **gpt-4o** | **gpt-4o-mini** |
+| --- | --- | --- | --- | --- | --- | --- |
+|Global & data zone provisioned minimum deployment|15|15|15|15|15|15|
+|Global & data zone provisioned scale increment|5|5|5|5|5|5|
+|Regional provisioned minimum deployment|50|25|25|25|50|25|
+|Regional provisioned scale increment|50|25|25|50|50|25|
+|Input TPM per PTU|3,000|14,900|2,500|230|2,500|37,000|
+|Latency Target Value|44 Tokens Per Second|50 Tokens Per Second| 66 Tokens Per Second |25 Tokens Per Second|25 Tokens Per Second|33 Tokens Per Second|
 
-|Topic| **gpt-4o**   | **gpt-4o-mini**  | **o1**| gpt-4.1 |
-| --- | --- | --- | --- | --- |
-|Global & data zone provisioned minimum deployment|15|15|15|15 |
-|Global & data zone provisioned scale increment|5|5|5| 5 | 
-|Regional provisioned minimum deployment|50|25|50| 50 |
-|Regional provisioned scale increment|50|25|50| 50 |
-|Input TPM per PTU |2,500|37,000|230| 3000 | 
-|Latency Target Value |25 Tokens Per Second|33 Tokens Per Second|25 Tokens Per Second| 44 Tokens Per Second |
 
 For a full list, see the [Azure OpenAI Service in Azure AI Foundry portal calculator](https://ai.azure.com/resource/calculator).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングされたスループットの仕様更新"
}
```

### Explanation
この修正は、Azure OpenAIサービスにおけるプロビジョニングされたスループットの仕様に関する情報を更新したものです。具体的には、各モデルのスループットに関する詳細情報が追加され、表形式で提示されるようになりました。

変更内容には、以下のような主な要素が含まれています：
- 各モデル（`gpt-4.1`、`gpt-4.1-mini`、`o3-mini`、`o1`、`gpt-4o`、`gpt-4o-mini`）に対して、グローバルおよびデータゾーンの最小プロビジョニングデプロイメント、スケールインクリメント、地域ごとの同様の情報、およびトークン毎分（TPM）の入力量とレイテンシターゲット値が新たに追加されました。
  
この情報の更新により、ユーザーはプロビジョニングされたスループットの具体的なパラメータを容易に理解し、自身のニーズに応じたモデル選択や設定が可能になるため、特にシステムのパフォーマンスを重視する利用者にとって有益です。全体として、ドキュメントの内容が最新化され、利便性が向上しています。

## articles/ai-services/openai/how-to/use-blocklists.md{#item-e99db7}

<details>
<summary>Diff</summary>
````diff
@@ -148,7 +148,7 @@ In the below example, a GPT-35-Turbo deployment with a blocklist is blocking the
         "status": 400, 
         "innererror": { 
             "code": "ResponsibleAIPolicyViolation", 
-            "content_filter_result": { 
+            "content_filter_results": { 
                 "custom_blocklists": [ 
                     { 
                         "filtered": true, 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ブロックリストのレスポンスフィールドの修正"
}
```

### Explanation
この修正は、Azure OpenAIサービスにおけるブロックリスト機能に関するドキュメント内での内容を更新したものです。具体的には、エラーレスポンスのJSONフィールドにおいて「content_filter_result」が「content_filter_results」に変更されました。

この変更により、複数のフィルタリング結果を含む可能性を示すために、フィールド名が単数形から複数形に修正されました。これにより、ブロックリスト機能に関連する情報がより正確に表現され、利用者が理解しやすくなります。

このような小規模な変更ながら、正確な情報提供を目指す上で重要な修正です。ドキュメント全体の整合性が向上し、ユーザーがエラーメッセージの解析を行う際に、正しいフィールド名に基づいて作業を進められるようになります。

## articles/ai-services/openai/includes/language-overview/python.md{#item-9cca6c}

<details>
<summary>Diff</summary>
````diff
@@ -336,7 +336,7 @@ print(completion.model_dump_json(indent=2))
   "prompt_filter_results": [
     {
       "prompt_index": 0,
-      "content_filter_result": {
+      "content_filter_results": {
         "jailbreak": {
           "filtered": false,
           "detected": false
@@ -345,7 +345,7 @@ print(completion.model_dump_json(indent=2))
     },
     {
       "prompt_index": 1,
-      "content_filter_result": {
+      "content_filter_results": {
         "sexual": {
           "filtered": false,
           "severity": "safe"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonコード内のレスポンスフィールドの修正"
}
```

### Explanation
この修正は、Azure OpenAIサービスに関するPythonコードのドキュメントにおいて、エラーレスポンスに関するフィールド名を更新したものです。具体的には、「content_filter_result」が「content_filter_results」に変更されました。

この変更により、レスポンスが複数のフィルタリング結果を含む可能性があることが示され、情報の正確性が向上しました。具体的には、`prompt_filter_results`の中で、各プロンプトに対するフィルタリング結果を正確に表現するために、フィールド名を複数形に修正しています。

このようなマイナーな変更ではありますが、正確な情報提供を目指す上で非常に重要です。利用者がPythonコードを実装する際に、最新のレスポンス形式に基づいて正確に処理を行うことができるため、ドキュメントの整合性と信頼性が高まります。

## articles/ai-services/openai/includes/model-matrix/datazone-provisioned-managed.md{#item-ae7f5b}

<details>
<summary>Diff</summary>
````diff
@@ -9,18 +9,19 @@ ms.custom: references_regions
 ms.date: 05/05/2025
 ---
 
-| **Region**     | **gpt-4.1**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:---------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| eastus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                        | -                       | -                  | -                      | -                      | -                      | -                           |
-| northcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+
+| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                        | -                            | -                       | -                  | -                      | -                      | -                      | -                           |
+| northcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの更新"
}
```

### Explanation
この修正は、Azure OpenAIサービスに関するモデルマトリックスのドキュメント内で、地域と利用可能なモデルの情報を更新したものです。主な変更点は、利用可能なモデル名とそのバージョンが改訂されたことです。

具体的には、モデルのバージョンの列に「gpt-4.1-mini」が追加され、既存の「o3-mini」や「gpt-4o」などのモデル名が見直されています。これにより、各地域におけるモデルの提供状況がより正確に反映され、利用者が選択できるオプションが明確になりました。

このような小規模な変更によって、ユーザーが最新の情報を基にモデルを選択する際の利便性が向上します。情報の透明性が高まり、Azure OpenAIサービスの利用者にとって有用な更新となっています。

## articles/ai-services/openai/includes/model-matrix/datazone-standard.md{#item-188333}

<details>
<summary>Diff</summary>
````diff
@@ -9,18 +9,18 @@ ms.custom: references_regions
 ms.date: 04/02/2025
 ---
 
-| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| eastus             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                        | ✅                   | -                      | -                      | ✅                       | ✅                            |
-| northcentralus     | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
+| **Region**     | **gpt-4.1-nano**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| eastus             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                             | ✅                        | ✅                   | -                      | -                      | ✅                       | ✅                            |
+| northcentralus     | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスのバージョン更新"
}
```

### Explanation
この修正は、Azure OpenAIサービスにおけるモデルマトリックスのドキュメントに対するもので、特にモデル名とバージョン情報の変更が行われています。主な変更点は、新しいモデル「gpt-4.1-nano」が追加されたことで、各地域における利用可能なモデルのリストが更新された点です。

新しいカラムが追加され、地域ごとの利用可否が示されており、利用者は最新のモデルの選択肢を視覚的に把握できるようになっています。具体的には、各地域において「gpt-4.1-nano」モデルが提供されているかどうかがリストに反映されています。

この更新により、ユーザーは新たに追加されたモデルを含む最新の情報に基づいて、適切なモデルを選択できるため、クラウドサービスの利用価値が向上します。情報の更新は、サービスの透明性と利用者の選択肢にとって非常に重要であり、これによりより良いユーザー体験が提供されます。

## articles/ai-services/openai/includes/model-matrix/global-batch.md{#item-929e6a}

<details>
<summary>Diff</summary>
````diff
@@ -10,26 +10,26 @@ ms.date: 04/21/2025
 ---
 
 
-| **Region**     | **o3-mini**, **2025-01-31**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-------------------|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| brazilsouth        | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| canadaeast         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| eastus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| eastus2            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| francecentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| germanywestcentral | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| japaneast          | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| koreacentral       | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| northcentralus     | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| norwayeast         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| polandcentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southafricanorth   | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southcentralus     | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| southindia         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| swedencentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| switzerlandnorth   | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| uksouth            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | -                      | ✅                       | ✅                       |
-| westeurope         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
-| westus3            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                            | ✅                       | ✅                       | ✅                       |
+| **Region**     | **o3-mini**, **2025-01-31**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| australiaeast      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadaeast         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| japaneast          | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| koreacentral       | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| norwayeast         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| southindia         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandnorth   | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| uksouth            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グローバルバッチモデルマトリックスの更新"
}
```

### Explanation
この修正は、Azure OpenAIサービスに関するグローバルバッチモデルマトリックスのドキュメントの更新です。主に、モデルのバージョン情報が見直され、各地域で提供されるモデルのリストが整理されました。

具体的な変更点として、新しいモデル列が追加されたわけではありませんが、既存のモデル情報が整理され、視認性が向上しています。すべての地域において、利用可能なモデル「o3-mini」、「gpt-4o」などの情報が一貫して表示されています。また、地域ごとのチェックマークが更新され、どのモデルがどの地域で利用可能かが明確に示されています。

これにより、ユーザーは利用可能なモデルの状況を迅速に把握でき、判断材料を持つことでサービスの選択が容易になります。ドキュメントの整頓によって、モデルマトリックスがさらに明確になり、利用者にとっての利便性が向上します。

## articles/ai-services/openai/includes/model-matrix/provisioned-global.md{#item-340884}

<details>
<summary>Diff</summary>
````diff
@@ -9,31 +9,31 @@ ms.custom: references_regions
 ms.date: 05/05/2025
 ---
 
-| **Region**     | **gpt-4.1**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
-|:-------------------|:---------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
-| australiaeast      | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| brazilsouth        | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| canadaeast         | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| eastus2            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| francecentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| germanywestcentral | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| italynorth         | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| japaneast          | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| koreacentral       | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| northcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| norwayeast         | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| polandcentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southafricanorth   | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southcentralus     | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southeastasia      | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| southindia         | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| spaincentral       | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| swedencentral      | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandnorth   | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| switzerlandwest    | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uaenorth           | ✅                       | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| uksouth            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westeurope         | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus             | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
-| westus3            | ✅                        | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   |
+|:-------------------|:---------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|
+| australiaeast      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| brazilsouth        | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| canadaeast         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| eastus2            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| francecentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| germanywestcentral | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| italynorth         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| japaneast          | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| koreacentral       | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| northcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| norwayeast         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| polandcentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southafricanorth   | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southcentralus     | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southeastasia      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| southindia         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| spaincentral       | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| swedencentral      | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandnorth   | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| switzerlandwest    | ✅                        | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uaenorth           | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| uksouth            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westeurope         | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus             | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
+| westus3            | ✅                        | ✅                             | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニング済みモデルマトリックスの更新"
}
```

### Explanation
この修正は、Azure OpenAIサービスのプロビジョニング済みモデルマトリックスにおける更新で、利用可能なモデルの情報が整理されています。具体的には、「gpt-4.1-mini」モデルが新たに追加され、これに伴い、各モデルのバージョンと対応地域が再整理されました。

主な変更点は以下の通りです：
- 新しいモデル「gpt-4.1-mini」が追加されたことにより、各地域のチェックマークが更新されています。
- 複数のモデルのバージョン情報が一貫して整理され、視認性が向上しました。
- また、特定の地域での利用可能モデルの情報がクリアに示されており、ユーザーがどの地域でどのモデルが使用可能かを簡単に理解できるようになっています。

このような更新により、ユーザーは最新のモデル情報を容易に把握でき、サービス選択の際の参考にすることができるため、利便性が向上します。全体として、ドキュメントの整然とした情報提供が、ユーザー体験の向上に寄与しています。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -6,33 +6,34 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 02/28/2025
+ms.date: 05/07/2025
 ---
 
-| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
-|:-------------------|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| brazilsouth        | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
-| canadaeast         | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
-| eastus             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| eastus2            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| francecentral      | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
-| germanywestcentral | -                       | -                  | ✅                       | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
-| japaneast          | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
-| koreacentral       | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| northcentralus     | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| norwayeast         | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
-| polandcentral      | -                       | -                  | ✅                       | -                      | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| southafricanorth   | -                       | -                  | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
-| southcentralus     | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| southeastasia      | -                       | -                  | -                      | ✅                       | ✅                       | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
-| southindia         | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
-| spaincentral       | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
-| swedencentral      | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandnorth   | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| switzerlandwest    | -                       | -                  | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
-| uaenorth           | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
-| uksouth            | -                       | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westeurope         | -                       | -                  | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                           | -                   | -                      | -                      |
-| westus             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus3            | -                       | -                  | ✅                       | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+
+| **Region**     | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
+|:-------------------|:---------------------------:|:--------------------------------:|:---------------------------:|:----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
+| australiaeast      | -                       | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| brazilsouth        | -                       | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | -                      |
+| canadaeast         | -                       | -                            | ✅                        | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | -                       | ✅                            | -                   | ✅                       | -                      |
+| eastus             | ✅                        | ✅                             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| eastus2            | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| francecentral      | -                       | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | -                      | ✅                       |
+| germanywestcentral | -                       | -                            | -                       | -                  | ✅                       | ✅                       | -                      | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | -                      |
+| japaneast          | -                       | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | -               | ✅                        | ✅                        | ✅                            | -                   | -                      | ✅                       |
+| koreacentral       | -                       | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | -                       | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| northcentralus     | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| norwayeast         | -                       | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | -                       | ✅                        | -                           | ✅                    | -                      | -                      |
+| polandcentral      | -                       | -                            | -                       | -                  | ✅                       | -                      | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southafricanorth   | -                       | -                            | -                       | -                  | ✅                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                            | ✅                    | ✅                       | -                      |
+| southcentralus     | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| southeastasia      | -                       | -                            | -                       | -                  | -                      | ✅                       | ✅                       | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | -                      |
+| southindia         | -                       | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | -                           | ✅                    | ✅                       | ✅                       |
+| spaincentral       | -                       | -                            | -                       | -                  | ✅                       | ✅                       | -                      | ✅                            | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| swedencentral      | -                       | ✅                             | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandnorth   | -                       | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| switzerlandwest    | -                       | -                            | -                       | -                  | -                      | -                      | -                      | -                           | -               | -                       | -                       | -                           | -                   | -                      | ✅                       |
+| uaenorth           | -                       | -                            | ✅                        | ✅                   | ✅                       | ✅                       | ✅                       | -                           | -               | ✅                        | -                       | -                           | -                   | ✅                       | ✅                       |
+| uksouth            | -                       | -                            | -                       | ✅                   | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westeurope         | -                       | -                            | -                       | -                  | -                      | -                      | ✅                       | -                           | -               | -                       | -                       | -                           | -                   | -                      | -                      |
+| westus             | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | ✅                            | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
+| westus3            | ✅                        | -                            | -                       | -                  | ✅                       | ✅                       | ✅                       | -                           | ✅                | ✅                        | ✅                        | ✅                            | ✅                    | ✅                       | ✅                       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニングモデルマトリックスの更新"
}
```

### Explanation
この修正は、Azure OpenAIサービスのプロビジョニングモデルマトリックスに実施された更新で、提供されるモデルの詳細と利用可能地域に関する情報が変更されています。具体的には、複数のモデルバージョンと地域ごとの利用状況が見直され、新しいモデルが追加されることで情報が整理されています。

主な変更点には以下が含まれます：
- 新しいモデル「gpt-4.1」とその関連情報が追加されました。
- モデルの利用可能地域についての情報が細かく更新され、一部地域におけるモデルの可用性が変更されました。
- 特定のモデルや地域に関するデータが整理され、視認性が向上しています。
- 更新日付が「2025年5月7日」に変更され、最新の内容が反映されています。

これらの変更により、ユーザーは最新のモデル情報を把握しやすくなり、利用可能なモデルを選定する際の判断が容易になります。また、モデルの配信状況が明確になることで、サービスの選択に役立つ情報が提供されています。全体的に、ドキュメントの明確な更新は、ユーザー体験の向上に寄与しています。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -9,29 +9,30 @@ ms.custom: references_regions
 ms.date: 04/17/2025
 ---
 
+
 | **Region**     | **o3**, **2025-04-16**   | **o4-mini**, **2025-04-16**   | **gpt-image-1**, **2025-04-15**   | **gpt-4.1**, **2025-04-14**   | **gpt-4.1-nano**, **2025-04-14**   | **gpt-4.1-mini**, **2025-04-14**   | **computer-use-preview**, **2025-03-11**   | **gpt-4.5-preview**, **2025-02-27**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4o-transcribe**, **2025-03-20**   | **gpt-4o-mini-tts**, **2025-03-20**   | **gpt-4o-mini-transcribe**, **2025-03-20**   |
 |:-------------------|:----------------------:|:---------------------------:|:-------------------------------:|:---------------------------:|:--------------------------------:|:--------------------------------:|:----------------------------------------:|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------------:|:-----------------------------------:|:------------------------------------------:|
 | australiaeast      | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | brazilsouth        | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| canadaeast         | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| canadaeast         | -                  | -                       | -                           | ✅                        | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | eastus             | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | ✅                                          | -                                 | -                               | -                                      |
 | eastus2            | ✅                   | ✅                        | -                           | ✅                        | ✅                             | ✅                             | ✅                                     | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                                  | ✅                                | ✅                                       |
 | francecentral      | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | germanywestcentral | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | italynorth         | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                           | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | japaneast          | -                  | -                       | -                           | ✅                        | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | koreacentral       | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| northcentralus     | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| northcentralus     | -                  | -                       | -                           | ✅                        | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | norwayeast         | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | polandcentral      | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | southafricanorth   | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| southcentralus     | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| southcentralus     | -                  | -                       | -                           | ✅                        | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | southindia         | -                  | -                       | -                           | -                       | -                            | -                            | ✅                                     | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | spaincentral       | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | swedencentral      | ✅                   | ✅                        | -                           | ✅                        | ✅                             | ✅                             | ✅                                     | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                                  | -                               | ✅                                       |
-| switzerlandnorth   | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
+| switzerlandnorth   | -                  | -                       | -                           | ✅                        | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | uaenorth           | -                  | -                       | ✅                            | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | uksouth            | -                  | -                       | -                           | ✅                        | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | westeurope         | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
 | westus             | -                  | -                       | -                           | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
-| westus3            | -                  | -                       | ✅                            | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -             
\ No newline at end of file
+| westus3            | -                  | -                       | ✅                            | -                       | -                            | -                            | -                                    | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                            | ✅                              | ✅                              | ✅                              | -                                       | -                                    | -                                            | -                                         | -                                 | -                               | -                                      |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準モデルマトリックスの更新"
}
```

### Explanation
この修正は、Azure OpenAIの標準モデルマトリックスにおいて、提供されるモデルの一覧とその利用可能地域に関する情報が更新されています。主な変更は、新しいモデルの追加と既存モデルの可用性の見直しが行われ、より詳細な情報が反映されています。

以下が主要な変更点です：
- 新しいモデル「gpt-4.1」、「gpt-4.1-nano」、「gpt-4.1-mini」などが追加され、リストの中でこれらのモデルが更新された提供日と共に記載されています。
- 一部地域において、特定のモデルの可用性が変更され、これによりユーザーが地域ごとに利用できるモデルの選定が容易になります。
- 「canadaeast」、「northcentralus」などの地域におけるモデルの利用可否が見直され、新たに利用可能になったモデルがあります。
- 更新日付が「2025年4月17日」に変更され、最新の情報が反映されています。

この更新によって、ユーザーは最新のモデルの可用情報を容易に把握でき、サービス選択においてより正確な情報に基づいて判断することができるようになります。ドキュメントの整然とした更新は、ユーザー体験の向上に寄与しています。


