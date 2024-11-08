---
date: '2024-11-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8be6320...MicrosoftDocs:6e04dd6
summary: |-
  この記事では、Azure OpenAIのドキュメントに関する3つのマイナーアップデートについて簡単に説明します。これらの変更は主に表現の改善を目的としており、具体的には次のポイントが含まれています。

  1. `gpt-4o`および`gpt-4o-mini`モデルのPTUごとのスループットに関する説明が明確にされました。
  2. JavaScriptにおけるAPIキーの認証方法が現在の情報と過去の情報から整理され、より理解しやすくなりました。
  3. クォータに関する役割の重要性がより明確にされ、ユーザーがAzure OpenAIの利用制限を適切に管理できるよう支援されています。

  新機能はありませんが、既存機能に関する説明が改善され、互換性に影響を与える重要な変更もありません。全体として、ユーザーがサービスを理解しやすくするための表現の見直しが行われており、エンドユーザーの体験向上を目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8be6320...MicrosoftDocs:6e04dd6){target="_blank"}

# ハイライト

この記事では、Azure OpenAI のドキュメントにおける3つのマイナーアップデートについて説明します。これらの変更は主に表現の改善に焦点を当てており、以下のようなポイントがあります:

1. **PTUごとのスループット**: `gpt-4o`および`gpt-4o-mini`モデルについて、スループット計算に関する説明がより明確に。
2. **APIキーの認証方法**: JavaScriptにおけるAPIキー認証方法の現状と過去の情報を明確化。
3. **クォータ情報の重要性**: 管理に必要な役割をより分かりやすく提案。

## 新機能

特定の新機能の追加はありませんが、既存機能の使用に関する説明が改善されました。

## 互換性に関する変更

特に互換性に影響を与える重要な変更は記載されていません。

## その他の更新

既存の情報がユーザーにとってより理解しやすくなるように表現が改良されました。

# インサイト

技術文書の表現は、エンドユーザーがサービスを理解し適切に利用する上で重要な役割を果たします。今回の変更は、主に既存の情報をより明確に伝えるものであり、ユーザーエクスペリエンスの向上を目的としています。

最初の変更では、プロビジョンされたスループットの説明がより具体的になり、ユーザーがPTU(プロビジョン済みトランザクションユニット)ごとの負荷を適切に測定できるようになっています。このような変更は、より正確なリソース管理に寄与します。

次に、JavaScriptにおけるAPIキー認証方法についての更新は、セキュアな認証手法の利用を促進します。APIキーは便利なものの、安全性に課題があるため、ドキュメントは推奨される実践的な方法を提供し、ユーザーに注意を促します。

最後に、クォータシステムの役割についての記載の改善は、アクセス管理を確実にし、ユーザーがAzure OpenAIで利用制限を管理するための主導権を握れるようにサポートします。役割の具体的な指針を示すことで、混乱を減らし、実際の運用におけるエラーを防ぐことができます。

これにより、ユーザーがより簡潔に正しい情報を得て、サービスをより効率的に利用することが可能となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [provisioned-throughput.md](#item-022e0c) | minor update | PTUごとのスループットに関するテーブルの説明を改善 | modified | 3 | 3 | 6 | 
| [migration-javascript.md](#item-19dac7) | minor update | APIキーの認証方法に関する情報の更新 | modified | 2 | 2 | 4 | 
| [quota.md](#item-9440c2) | minor update | クォータ情報の重要性に関する表現の改善 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/provisioned-throughput.md{#item-022e0c}

<details>
<summary>Diff</summary>
````diff
@@ -41,13 +41,13 @@ An Azure OpenAI Deployment is a unit of management for a specific OpenAI Model.
 ## How much throughput per PTU you get for each model
 The amount of throughput (tokens per minute or TPM) a deployment gets per PTU is a function of the input and output tokens in the minute. Generating output tokens requires more processing than input tokens and so the more output tokens generated the lower your overall TPM. The service dynamically balances the input & output costs, so users do not have to set specific input and output limits. This approach means your deployment is resilient to fluctuations in the workload shape. 
 
-To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models. The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page].(https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
+To help with simplifying the sizing effort, the following table outlines the TPM per PTU for the `gpt-4o` and `gpt-4o-mini` models which represent the max all the traffic is either input or output. The table also shows Service Level Agreement (SLA) Latency Target Values per model.  For more information about the SLA for Azure OpenAI Service, see the [Service Level Agreements (SLA) for Online Services page].(https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1)
 
 |     | **gpt-4o**, **2024-05-13**   & **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   |
 | --- | --- | --- |
 | Deployable Increments | 50 | 25|
-| Input TPM per PTU | 2,500 | 37,000  |
-| Output TPM per PTU| 833|12,333|
+|Max Input TPM per PTU | 2,500 | 37,000  |
+|Max Output TPM per PTU| 833|12,333|
 | Latency Target Value |25 Tokens Per Second* |33 Tokens Per Second*|
 
 For a full list see the [AOAI Studio calculator](https://oai.azure.com/portal/calculator).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PTUごとのスループットに関するテーブルの説明を改善"
}
```

### Explanation
この変更は、Azure OpenAI デプロイメントのスループットについての説明を明確にするためのマイナーアップデートです。具体的には、`gpt-4o`および`gpt-4o-mini`モデルに関するテーブルの表現が改善されました。元のテキストでは「入力および出力トークンが含まれる」という表現が使用されていましたが、新しい表現では「すべてのトラフィックが入力または出力であることを示す最大値」という形に変更され、情報が明確になっています。この変更は、ユーザーがスループットの設定を簡単に理解できるようにするためのものであり、またサービスの遅延ターゲット値とSLA リンクが引き続き提供されています。このようにして、ユーザーはAzure OpenAIサービスの能力をより適切に評価することができます。

## articles/ai-services/openai/how-to/migration-javascript.md{#item-19dac7}

<details>
<summary>Diff</summary>
````diff
@@ -43,14 +43,14 @@ const azureADTokenProvider = getBearerTokenProvider(credential, scope);
 
 ### (Highly Discouraged) API Key
 
-API keys are not recommended for production use because they are less secure than other authentication methods. However, if you are using an API key to authenticate `OpenAIClient` or `AssistantsClient`, an `AzureKeyCredential` object must be created as follows:
+API keys are not recommended for production use because they are less secure than other authentication methods. Previously, `AzureKeyCredential` objects were created as follows to authenticate `OpenAIClient` or `AssistantsClient`:
 
 ```typescript
 import { AzureKeyCredential } from "@azure/openai";
 const apiKey = new AzureKeyCredential("your API key");
 ```
 
-Authenticating `AzureOpenAI` with an API key involves setting the `AZURE_OPENAI_API_KEY` environment variable or setting the `apiKey` string property in the options object when creating the `AzureOpenAI` client.
+On the other hand, `AzureOpenAI` can be authenticated with an API key by setting the `AZURE_OPENAI_API_KEY` environment variable or by setting the `apiKey` string property in the options object when creating the `AzureOpenAI` client.
 
 [!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIキーの認証方法に関する情報の更新"
}
```

### Explanation
この変更は、JavaScript における Azure OpenAI クライアントの API キー認証方法に関する情報を更新するためのマイナーアップデートです。具体的には、API キーが推奨されない理由を説明する文が修正され、以前は `AzureKeyCredential` オブジェクトがどのように作成されていたのかを明確に示す形に変更されました。これにより、ユーザーは現在の推奨される認証方法と過去の方法の違いを理解しやすくなっています。また、`AzureOpenAI` に対する API キーによる認証方法の説明も若干の表現変更がなされており、より明確な言い回しに更新されています。この変更によって、ドキュメントの情報が最新の状況により適合するようになり、利用者が正確に理解できる手助けとなることを目的としています。

## articles/ai-services/openai/how-to/quota.md{#item-9440c2}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ Quota provides the flexibility to actively manage the allocation of rate limits
 ## Prerequisites
 
 > [!IMPORTANT]
-> Viewing quota and deploying models requires the **Cognitive Services Usages Reader** role. This role provides the minimal access necessary to view quota usage across an Azure subscription. To learn more about this role and the other roles you will need to access Azure OpenAI, consult our [Azure role-based access (Azure RBAC) guide](./role-based-access-control.md).
+> For any task that requires viewing available quota we recommend using the **Cognitive Services Usages Reader** role. This role provides the minimal access necessary to view quota usage across an Azure subscription. To learn more about this role and the other roles you will need to access Azure OpenAI, consult our [Azure role-based access (Azure RBAC) guide](./role-based-access-control.md). 
 >
 > This role can be found in the Azure portal under **Subscriptions** > **Access control (IAM)** > **Add role assignment** > search for **Cognitive Services Usages Reader**.This role **must be applied at the subscription level**, it does not exist at the resource level.
 >
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータ情報の重要性に関する表現の改善"
}
```

### Explanation
この変更は、Azure OpenAIのクォータに関するセクションの重要な情報をわかりやすくするためのマイナーアップデートです。具体的には、「クォータを表示するための役割」として以前の表現を修正し、「利用可能なクォータを表示する必要があるタスクには、**Cognitive Services Usages Reader** ロールを使用することを推奨します」と明確に指示する形に更新されました。この更新により、クォータの管理に必要な役割の認識が向上し、ユーザーが必要な役割を正確に把握しやすくなります。また、ロールの設定方法に関する説明は変更されていませんが、より明確なコンテキストが追加されており、情報全体の理解を助ける構成となっています。これにより、Azure OpenAI に対するアクセス管理が一層容易になります。


