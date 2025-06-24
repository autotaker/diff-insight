---
date: '2025-06-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fb526ea...MicrosoftDocs:db5cbff
summary: 今回の更新は、Azure OpenAIサービスに関するドキュメントの情報を正確にし、ユーザーの理解を向上させることを目的としています。主な変更点は、「overview.md」に新しいセクションとして「画像生成トークン」が追加されたことと、関連ドキュメントのリンク修正です。これにより、クォータや制限に関する情報が細分化され、ユーザーがサービスを効果的に利用できるためのガイドラインが提供されました。全体として、より良い情報提供が目指されており、Azure
  OpenAIサービスの利用が便利で効率的になることが期待されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fb526ea...MicrosoftDocs:db5cbff){target="_blank"}

# ハイライト
今回の更新は、複数のドキュメントに若干の情報追加とリンク修正を行うことにより、Azure OpenAIサービスに関する情報の正確性およびユーザーの理解を向上させることが目的です。変更点には、新しいセクションの追加やリンクテキストの変更などがあります。

## 新機能
- `overview.md` における「画像生成トークン」に関する新しいセクションの追加。

## 破壊的な変更
- なし。

## その他の更新
- `dall-e.md` と `gpt-with-vision.md`のリンク及びテキストが修正され、情報がクリアで正確になりました。
- `quota.md` と `quotas-limits.md` において、クォータや制限に関する情報が細分化され、ユーザーがより具体的にサービスを活用するためのガイドラインが提供されました。

# インサイト
この差分は、主にAzure OpenAIのサービスを利用するユーザー向けに、ドキュメントの情報をより正確で理解しやすくするための更新です。特に、サービスの利用におけるトークンやリクエストのコストや制限に関する情報がアップデートされており、ユーザーはこれらを参考にして効率的なリソース管理を行うことができます。

例えば、`overview.md`に新しく追加された「画像生成トークン」に関するセクションでは、指定されたモデル（GPT-image-1 に限らず）が生成する画像のために必要なトークン数が具体的に示されており、これによりユーザーはコストを予測しやすく、予算内で効率よくサービスを活用することが可能になります。

また、リンクの修正はユーザーエクスペリエンスの向上に寄与しており、特に技術文書の文脈に応じた内容の正確な理解を助けています。誤解を招きやすいリンクテキストを修正することにより、ユーザーが必要な情報を迅速に取得できるよう配慮されています。

全体として、今回の更新はユーザーに対してより良い情報提供を行うために設計されており、ドキュメントが提供する情報の品質向上を意図しています。これにより、Azure OpenAIサービスの利用がより簡単かつ効率的になり、特に商業利用や学術研究のコンテキストにおいて、その有用性が高まると期待されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [dall-e.md](#item-ac9616) | minor update | DALL·E に関する追加情報の掲載 | modified | 4 | 0 | 4 | 
| [gpt-with-vision.md](#item-4d8502) | minor update | 画像入力トークンに関するリンクの修正 | modified | 1 | 1 | 2 | 
| [quota.md](#item-9440c2) | minor update | クォータ情報の更新とリンクの修正 | modified | 23 | 10 | 33 | 
| [overview.md](#item-97d507) | minor update | 画像トークンおよび画像生成トークンに関する情報の追加 | modified | 13 | 1 | 14 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限に関する情報の更新 | modified | 11 | 12 | 23 | 


# Modified Contents
## articles/ai-services/openai/how-to/dall-e.md{#item-ac9616}

<details>
<summary>Diff</summary>
````diff
@@ -100,6 +100,10 @@ The following is a sample request body. You specify a number of options, defined
 
 ---
 
+> [!TIP]
+> For image generation token costs, see [Image tokens](../overview.md#image-generation-tokens).
+
+
 ### Output
 
 The response from a successful image generation API call looks like the following example. The `url` field contains a URL where you can download the generated image. The URL stays active for 24 hours.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·E に関する追加情報の掲載"
}
```

### Explanation
このコードの差分は、DALL·Eに関するドキュメントに4行の新しい情報が追加されたことを示しています。具体的には、提案されたチップとして「画像生成トークン費用」に関するリンクを追加しました。この追加により、ユーザーはトークンのコストに関する情報を簡単に参照できるようになります。文書の内容は強化され、利用者が画像生成に関連するコストについて理解を深められるようになりました。この変更は機能を壊すことなく、既存のコンテンツを改善するものです。

## articles/ai-services/openai/how-to/gpt-with-vision.md{#item-4d8502}

<details>
<summary>Diff</summary>
````diff
@@ -181,7 +181,7 @@ You set the value using the format shown in this example:
 }
 ```
 
-For details on how the image parameters impact tokens used and pricing please see - [What is Azure OpenAI? Image Tokens](../overview.md#image-tokens)
+For details on how the image parameters impact tokens used and pricing please see - [What is Azure OpenAI? Image Tokens](../overview.md#image-input-tokens)
 
 
 ## Output
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像入力トークンに関するリンクの修正"
}
```

### Explanation
このコードの差分は、GPTとビジョンに関するドキュメント内のリンクテキストの修正を示しています。具体的には、画像パラメータが使用するトークンと価格に与える影響に関する詳細情報へのリンクが更新され、"Image Tokens"から"Image Input Tokens"に変更されました。この修正により、リンク先の内容がより正確に反映されるようになり、読み手が混乱しないように配慮されています。逆に、情報の明確さが向上し、ユーザーが適切な情報を得る助けとなります。

## articles/ai-services/openai/how-to/quota.md{#item-9440c2}

<details>
<summary>Diff</summary>
````diff
@@ -16,11 +16,11 @@ Quota provides the flexibility to actively manage the allocation of rate limits
 ## Prerequisites
 
 > [!IMPORTANT]
-> For any task that requires viewing available quota we recommend using the **Cognitive Services Usages Reader** role. This role provides the minimal access necessary to view quota usage across an Azure subscription. To learn more about this role and the other roles you will need to access Azure OpenAI, consult our [Azure role-based access control guide](./role-based-access-control.md). 
+> For any task that requires viewing available quota we recommend using the **Cognitive Services Usages Reader** role. This role provides the minimal access necessary to view quota usage across an Azure subscription. To learn more about this role and the other roles you'll need to access Azure OpenAI, consult our [Azure role-based access control guide](./role-based-access-control.md). 
 >
-> This role can be found in the Azure portal under **Subscriptions** > **Access control (IAM)** > **Add role assignment** > search for **Cognitive Services Usages Reader**. This role **must be applied at the subscription level**, it does not exist at the resource level.
+> This role can be found in the Azure portal under **Subscriptions** > **Access control (IAM)** > **Add role assignment** > search for **Cognitive Services Usages Reader**. This role **must be applied at the subscription level**, it doesn't exist at the resource level.
 >
-> If you do not wish to use this role, the subscription **Reader** role will provide equivalent access, but it will also grant read access beyond the scope of what is needed for viewing quota and model deployment.
+> If you don't wish to use this role, the subscription **Reader** role will provide equivalent access, but it will also grant read access beyond the scope of what is needed for viewing quota and model deployment.
 
 ## Introduction to quota
 
@@ -31,7 +31,20 @@ Azure OpenAI's quota feature enables assignment of rate limits to your deploymen
 
 When a deployment is created, the assigned TPM will directly map to the tokens-per-minute rate limit enforced on its inferencing requests. A **Requests-Per-Minute (RPM)** rate limit will also be enforced whose value is set proportionally to the TPM assignment using the following ratio:
 
-6 RPM per 1000 TPM. (This ratio can vary by model for more information, see [quota, and limits](../quotas-limits.md#o-series-rate-limits).)
+> [!IMPORTANT]
+> The ratio of Requests Per Minute (RPM) to Tokens Per Minute (TPM) for quota can vary by model. When you deploy a model programmatically or [request a quota increase](https://aka.ms/oai/stuquotarequest) you don't have granular control over TPM and RPM as independent values. Quota is allocated in terms of units of capacity which have corresponding amounts of RPM & TPM:
+>
+> | Model                  | Capacity   | Requests Per Minute (RPM)  | Tokens Per Minute (TPM) |
+> |------------------------|:----------:|:--------------------------:|:-----------------------:|
+> | **Older chat models:** | 1 Unit     | 6 RPM                      | 1,000 TPM               |
+> | **o1 & o1-preview:**   | 1 Unit     | 1 RPM                      | 6,000 TPM               |
+> | **o3**                 | 1 Unit     | 1 RPM                      | 1,000 TPM               |
+> | **o4-mini**            | 1 Unit     | 1 RPM                      | 1,000 TPM               |
+> | **o3-mini:**           | 1 Unit     | 1 RPM                      | 10,000 TPM              |
+> | **o1-mini:**           | 1 Unit     | 1 RPM                      | 10,000 TPM              |
+> | **o3-pro:**            | 1 Unit     | 1 RPM                      | 10,000 TPM              |
+>
+> This is particularly important for programmatic model deployment as changes in RPM/TPM ratio can result in accidental  misallocation of quota. For more information, see [quota, and limits](../quotas-limits.md#o-series-rate-limits).
 
 The flexibility to distribute TPM globally within a subscription and region has allowed Azure OpenAI to loosen other restrictions:
 
@@ -62,7 +75,7 @@ Different model deployments, also called model classes have unique max TPM value
 All other model classes have a common max TPM value.
 
 > [!NOTE]
-> Quota Tokens-Per-Minute (TPM) allocation is not related to the max input token limit of a model. Model input token limits are defined in the [models table](../concepts/models.md) and are not impacted by changes made to TPM.  
+> Quota Tokens-Per-Minute (TPM) allocation isn't related to the max input token limit of a model. Model input token limits are defined in the [models table](../concepts/models.md) and aren't impacted by changes made to TPM.  
 
 ## View and request quota
 
@@ -92,7 +105,7 @@ As each request is received, Azure OpenAI computes an estimated max processed-to
 As requests come into the deployment endpoint, the estimated max-processed-token count is added to a running token count of all requests that is reset each minute. If at any time during that minute, the TPM rate limit value is reached, then further requests will receive a 429 response code until the counter resets.
 
 > [!IMPORTANT]
-> The token count used in the rate limit calculation is an estimate based in part on the character count of the API request. The rate limit token estimate is not the same as the token calculation that is used for billing/determining that a request is below a model's input token limit. Due to the approximate nature of the rate limit token calculation, it is expected behavior that a rate limit can be triggered prior to what might be expected in comparison to an exact token count measurement for each request.  
+> The token count used in the rate limit calculation is an estimate based in part on the character count of the API request. The rate limit token estimate isn't the same as the token calculation that is used for billing/determining that a request is below a model's input token limit. Due to the approximate nature of the rate limit token calculation, it's expected behavior that a rate limit can be triggered prior to what might be expected in comparison to an exact token count measurement for each request.  
 
 RPM rate limits are based on the number of requests received over time. The rate limit expects that requests be evenly distributed over a one-minute period. If this average flow isn't maintained, then requests might receive a 429 response even though the limit isn't met when measured over the course of a minute. To implement this behavior, Azure OpenAI evaluates the rate of incoming requests over a small period of time, typically 1 or 10 seconds. If the number of requests received during that time exceeds what would be expected at the set RPM limit, then new requests will receive a 429 response code until the next evaluation period. For example, if Azure OpenAI is monitoring request rate on 1-second intervals, then rate limiting will occur for a 600-RPM deployment if more than 10 requests are received during each 1-second period (600 requests per minute = 10 requests per second).
 
@@ -108,7 +121,7 @@ To minimize issues related to rate limits, it's a good idea to use the following
 
 ## Automate deployment
 
-This section contains brief example templates to help get you started programmatically creating deployments that use quota to set TPM rate limits. With the introduction of quota you must use API version `2023-05-01` for resource management related activities. This API version is only for managing your resources, and does not impact the API version used for inferencing calls like completions, chat completions, embedding, image generation, etc.
+This section contains brief example templates to help get you started programmatically creating deployments that use quota to set TPM rate limits. With the introduction of quota you must use API version `2023-05-01` for resource management related activities. This API version is only for managing your resources, and doesn't impact the API version used for inferencing calls like completions, chat completions, embedding, image generation, etc.
 
 # [REST](#tab/rest)
 
@@ -139,7 +152,7 @@ This is only a subset of the available request body parameters. For the full lis
 |Parameter|Type| Description |
 |--|--|--|
 |sku | Sku | The resource model definition representing SKU.|
-|capacity|integer|This represents the amount of [quota](../how-to/quota.md) you are assigning to this deployment. A value of 1 equals 1,000 Tokens per Minute (TPM). A value of 10 equals 10k Tokens per Minute (TPM).|
+|capacity|integer|This represents the amount of [quota](../how-to/quota.md) you're assigning to this deployment. A value of 1 equals 1,000 Tokens per Minute (TPM). A value of 10 equals 10k Tokens per Minute (TPM).|
 
 #### Example request
 
@@ -186,7 +199,7 @@ curl -X GET https://management.azure.com/subscriptions/00000000-0000-0000-0000-0
 
 Install the [Azure CLI](/cli/azure/install-azure-cli). Quota requires `Azure CLI version 2.51.0`. If you already have Azure CLI installed locally run `az upgrade` to update to the latest version.
 
-To check which version of Azure CLI you are running use `az version`. Azure Cloud Shell is currently still running 2.50.0 so in the interim local installation of Azure CLI is required to take advantage of the latest Azure OpenAI features.
+To check which version of Azure CLI you're running use `az version`. Azure Cloud Shell is currently still running 2.50.0 so in the interim local installation of Azure CLI is required to take advantage of the latest Azure OpenAI features.
 
 ### Deployment
 
@@ -239,7 +252,7 @@ For more information, see the [Azure CLI reference documentation](/cli/azure/cog
 
 Install the latest version of the [Az PowerShell module](/powershell/azure/install-azure-powershell). If you already have the Az PowerShell module installed locally, run `Update-Module -Name Az` to update to the latest version.
 
-To check which version of the Az PowerShell module you are running, use `Get-InstalledModule -Name Az`. Azure Cloud Shell is currently running a version of Azure PowerShell that can take advantage of the latest Azure OpenAI features.
+To check which version of the Az PowerShell module you're running, use `Get-InstalledModule -Name Az`. Azure Cloud Shell is currently running a version of Azure PowerShell that can take advantage of the latest Azure OpenAI features.
 
 ### Deployment
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータ情報の更新とリンクの修正"
}
```

### Explanation
このコードの差分は、Azure OpenAIのクォータに関する文書の一部が更新され、内容がより明確になったことを示しています。具体的には、クォータに関する重要な情報が追加され、リンクとその記述が修正されました。新しい情報には、モデルごとのリクエスト数とトークン数の比率に関する説明や、具体的な数値がテーブル形式で示されています。さらに、いくつかの文が簡潔になり、読み手にとって理解しやすくなっています。この変更は、クォータの管理や関連するロールの使用方法についての理解を深める助けとなり、ユーザーの便宜を図っています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -84,7 +84,7 @@ Azure OpenAI processes text by breaking it down into tokens. Tokens can be words
 
 The total number of tokens processed in a given request depends on the length of your input, output, and request parameters. The quantity of tokens being processed will also affect your response latency and throughput for the models.
  
-#### Image tokens
+#### Image input tokens
 
 Azure OpenAI's image processing capabilities with GPT-4o, GPT-4o-mini, and GPT-4 Turbo with Vision models uses image tokenization to determine the total number of tokens consumed by image inputs. The number of tokens consumed is calculated based on two main factors: the level of image detail (low or high) and the image’s dimensions. Here's how token costs are calculated:
 
@@ -108,6 +108,18 @@ Azure OpenAI's image processing capabilities with GPT-4o, GPT-4o-mini, and GPT-4
         - For GPT-4o and GPT-4 Turbo with Vision, the total token cost is 6 tiles x 170 tokens per tile + 85 base tokens = 1105 tokens.
         - For GPT-4o mini, the total token cost is 6 tiles x 5667 tokens per tile + 2833 base tokens = 36835 tokens.
 
+#### Image generation tokens 
+
+GPT-image-1 generates images by first producing specialized image tokens. Both latency and eventual cost are proportional to the number of tokens required to render an image. The number of tokens generated depends on image dimensions and quality:
+
+| Quality | Square (1024×1024) | Portrait (1024×1536) | landscape (1536×1024) |
+| ----------- | ---------------------- | ------------------------ | ------------------------- |
+| Low         | 272 tokens             | 408 tokens               | 400 tokens                |
+| Medium      | 1056 tokens            | 1584 tokens              | 1568 tokens               |
+| High        | 4160 tokens            | 6240 tokens              | 6208 tokens               |
+
+
+
 ### Resources
 
 Azure OpenAI is a new product offering on Azure. You can get started with Azure OpenAI the same way as any other Azure product where you [create a resource](how-to/create-resource.md), or instance of the service, in your Azure Subscription. You can read more about Azure's [resource management design](/azure/azure-resource-manager/management/overview).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像トークンおよび画像生成トークンに関する情報の追加"
}
```

### Explanation
このコードの差分は、Azure OpenAIに関するオーバービュー文書に新たな情報が追加されたことを示しています。具体的には、画像トークンという見出しが「画像入力トークン」に改名され、その下に画像処理に関連する詳細が記載されています。また、新たに「画像生成トークン」というセクションが追加され、GPT-image-1が生成する画像に対するトークン数の計算方法が説明されています。これは画像の品質やサイズに基づいてトークンの数が異なることを示しており、細かいトークン数のテーブルも提供されています。この変更は、ユーザーが画像処理のリソースを効果的に管理し、トークンのコストを理解するのに役立ちます。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -99,30 +99,29 @@ The following sections provide you with a quick guide to the default quotas and
 | `model-router` (2025-05-19) | Enterprise Tier | 10 M | 10 K |
 | `model-router` (2025-05-19) | Default         | 1 M | 1 K |
 
-
 ## computer-use-preview global standard rate limits
 
 | Model|Tier| Quota Limit in tokens per minute (TPM) | Requests per minute |
 |---|---|:---:|:---:|
 | `computer-use-preview`| Enterprise Tier | 30 M | 300 K |
 | `computer-use-preview`| Default         | 450 K | 4.5 K |
 
-
 ## o-series rate limits
 
 > [!IMPORTANT]
-> The ratio of RPM/TPM for quota with o1-series models works differently than older chat completions models:
->
-> - **Older chat models:** 1 unit of capacity = 6 RPM and 1,000 TPM.
-> - **o1 & o1-preview:** 1 unit of capacity = 1 RPM and 6,000 TPM.
-> - **o3** 1 unit of capacity = 1 RPM per 1,000 TPM
-> - **o4-mini** 1 unit of capacity = 1 RPM per 1,000 TPM
-> - **o3-mini:** 1 unit of capacity = 1 RPM per 10,000 TPM.
-> - **o1-mini:** 1 unit of capacity = 1 RPM per 10,000 TPM.
+> The ratio of Requests Per Minute (RPM) to Tokens Per Minute (TPM) for quota can vary by model. When you deploy a model programmatically or [request a quota increase](https://aka.ms/oai/stuquotarequest) you don't have granular control over TPM and RPM as independent values. Quota is allocated in terms of units of capacity which have corresponding amounts of RPM & TPM:
 >
-> This is particularly important for programmatic model deployment as this change in RPM/TPM ratio can result in accidental under allocation of quota if one is still assuming the 1:1000 ratio followed by older chat completion models.
+> | Model                  | Capacity   | Requests Per Minute (RPM)  | Tokens Per Minute (TPM) |
+> |------------------------|:----------:|:--------------------------:|:-----------------------:|
+> | **Older chat models:** | 1 Unit     | 6 RPM                      | 1,000 TPM               |
+> | **o1 & o1-preview:**   | 1 Unit     | 1 RPM                      | 6,000 TPM               |
+> | **o3**                 | 1 Unit     | 1 RPM                      | 1,000 TPM               |
+> | **o4-mini**            | 1 Unit     | 1 RPM                      | 1,000 TPM               |
+> | **o3-mini:**           | 1 Unit     | 1 RPM                      | 10,000 TPM              |
+> | **o1-mini:**           | 1 Unit     | 1 RPM                      | 10,000 TPM              |
+> | **o3-pro:**            | 1 Unit     | 1 RPM                      | 10,000 TPM              |
 >
-> There's a known issue with the [quota/usages API](/rest/api/aiservices/accountmanagement/usages/list?view=rest-aiservices-accountmanagement-2024-06-01-preview&tabs=HTTP&preserve-view=true) where it assumes the old ratio applies to the new o1-series models. The API returns the correct base capacity number, but doesn't apply the correct ratio for the accurate calculation of TPM.
+> This is particularly important for programmatic model deployment as changes in RPM/TPM ratio can result in accidental  misallocation of quota.
 
 ### o-series global standard
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限に関する情報の更新"
}
```

### Explanation
このコードの差分は、Azure OpenAIにおけるクォータと制限に関する文書のいくつかの重要な部分が更新されたことを示しています。具体的には、`computer-use-preview`モデルに関する情報が整理され、グローバルな標準レート制限セクションが新たに追加されています。また、oシリーズのモデルに対応したリクエスト毎分（RPM）とトークン毎分（TPM）の比率についての説明が詳化され、サンプルテーブルが含まれています。これにより、ユーザーは各モデルにおけるトークンとリクエストの制限をより明確に把握できるようになり、特にプログラムでのモデル展開時におけるクォータの割り当て誤差を防ぐための重要な情報が提供されています。全体として、文書はユーザーがクォータを正確に管理しやすくなるよう改善されています。


