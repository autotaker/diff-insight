---
date: '2024-09-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:41463e4...MicrosoftDocs:135d681
summary: このコードの変更は、複数のドキュメントに対する軽微な更新と新機能の追加を特徴としています。主な変更点には用語の統一や表現の明確化、新しいセクションや画像の追加が含まれています。操作方法の一貫性やユーザーが手順を理解しやすくするための変更が行われています。新しい画像ファイルが追加され、視覚的な指示が強化されています。また、用語の変更や文書のフォーマット修正も実施されていますが、大きな破壊的変更はありません。全体的に、ドキュメントの質が向上し、ユーザーが必要な情報を迅速かつ正確に取得できるようになっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:41463e4...MicrosoftDocs:135d681){target="_blank"}

# ハイライト
このコードの変更は、複数のドキュメントを対象にした軽微な更新および新機能の追加が特徴です。主な変更点として、用語の統一、表現の明確化、新しいセクションや画像の追加があります。特に注意事項は、操作方法の一貫性向上や、ユーザーが手順を容易に理解できるようにするための変更が多数施されています。

## 新機能
- 「delete-hub-button.png」などの新しい画像ファイルが追加され、視覚的な指示が強化されました。
- Azureポータルにおけるハブ管理手順やポータル内検索に関する画像が新規追加されました。

## 破壊的変更
特に大きな破壊的変更は見られませんが、用語の統一や表現の改善により、旧ドキュメントとの一部互換性が失われる可能性があります。

## その他の更新
- 用語の統一（例：「AIQ」を「モデル品質」に変更）
- 表現の明確化（例：「レシピ」を「トレーニング設定」に修正）
- 日付やフォーマットの修正（例：ドキュメントの日付更新、`response_format`の指定方法変更）
- TOC (Table of Contents) の再整理

# インサイト
このコードの更新は、一連のドキュメントを対象に、ユーザーが操作方法や概念をより理解しやすくするためのものです。変更点の大半は、用語の統一や表現の明確化にフォーカスしており、これによりユーザーが混乱することなく正確な情報を得られるようになっています。新しい画像の追加は特に視覚的支援を強化しており、操作手順を直感的に理解できるようになっています。

1. **用語の統一と表現の明確化**：
   - 「AIQ」から「モデル品質」への変更や、「レシピ」から「トレーニング設定」への変更は、用語がより一貫して使用され、ユーザーにとってわかりやすくなっています。
   - JSON出力フォーマットに関連する警告文がより具体的になり、誤解を与えないように改善されています。

2. **新しいセクションと画像の追加**：
   - Azure AI Studioのハブ削除方法など、新しいセクションの追加により操作ガイドがさらに充実しています。
   - 「delete-hub-button.png」や「manage-hub-azure-portal.png」などの画像は、ユーザーが実際の操作をイメージしやすくするとともに、手順の視認性を高めています。

3. **コードの一貫性と日付の更新**：
   - 日付の更新やフォーマットの統一は、最新の情報と一貫した表記を保証し、ドキュメント全体の信頼性を向上させています。
   - NuGetなどの専門用語の表記が統一され、ユーザーが混乱しないように配慮されています。

これらの変更により、ドキュメントの質は全体的に向上しており、ユーザーが必要な情報を迅速かつ正確に取得できるようになっています。特に、技術的な手順や設定に関する情報が明確化されており、実際の運用において非常に役立つ内容となっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [best-practices.md](#item-ae9331) | minor update | ベストプラクティス記事の軽微な更新 | modified | 6 | 6 | 12 | 
| [configure-private-link.md](#item-bbf93d) | minor update | プライベートリンク設定に関する軽微な修正 | modified | 0 | 2 | 2 | 
| [create-azure-ai-resource.md](#item-998abe) | minor update | Azure AI Studioハブの管理に関する情報の追加と修正 | modified | 20 | 3 | 23 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | JaisモデルのJSON出力フォーマットに関する情報の修正と詳細の追加 | modified | 10 | 10 | 20 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | Meta Llamaモデルに関する情報の修正と更新 | modified | 10 | 10 | 20 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | Mistral Nemoモデルに関する情報の更新 | modified | 8 | 8 | 16 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | Mistralモデルに関する情報の更新 | modified | 19 | 19 | 38 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralチャットモデルに関する情報の更新 | modified | 8 | 8 | 16 | 
| [deploy-models-phi-3-5-moe.md](#item-9af6ea) | minor update | Phi-3.5 MoEモデルに関する情報の更新 | modified | 2 | 2 | 4 | 
| [deploy-models-phi-3-vision.md](#item-bd5aae) | minor update | Phi-3ビジョンモデルに関する情報の更新 | modified | 2 | 2 | 4 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | Phi-3ファミリーチャットモデルに関する情報の更新 | modified | 2 | 2 | 4 | 
| [fine-tune-model-llama.md](#item-2a42d8) | minor update | Llamaモデルのファインチューニング手順の修正 | modified | 1 | 1 | 2 | 
| [delete-hub-button.png](#item-92c030) | new feature | ハブ削除ボタンの画像追加 | added | 0 | 0 | 0 | 
| [manage-hub-azure-portal.png](#item-8f34ee) | new feature | Azureポータルでのハブ管理に関する画像追加 | added | 0 | 0 | 0 | 
| [search-in-portal.png](#item-44ef96) | new feature | ポータル内検索に関する画像追加 | added | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | TOCファイルの更新：ハブ作成手順の整理 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/concepts/best-practices.md{#item-ae9331}

<details>
<summary>Diff</summary>
````diff
@@ -47,7 +47,7 @@ You also want to avoid mixing different schema designs. Don't build half of your
 
 ## Use standard training before advanced training
 
-[Standard training](../how-to/train-model.md#training-modes) is free and faster than advanced training. It can help you quickly understand the effect of changing your training set or schema while you build the model. After you're satisfied with the schema, consider using advanced training to get the best AIQ out of your model.
+[Standard training](../how-to/train-model.md#training-modes) is free and faster than advanced training. It can help you quickly understand the effect of changing your training set or schema while you build the model. After you're satisfied with the schema, consider using advanced training to get the best model quality.
 
 ## Use the evaluation feature
 
@@ -113,7 +113,7 @@ If you enable this feature, the utterance count of your training set increases.
 
 ## Address model overconfidence
 
-Customers can use the LoraNorm recipe version if the model is being incorrectly overconfident. An example of this behavior can be like the following scenario where the model predicts the incorrect intent with 100% confidence. This score makes the confidence threshold project setting unusable.
+Customers can use the LoraNorm traning configuration version if the model is being incorrectly overconfident. An example of this behavior can be like the following scenario where the model predicts the incorrect intent with 100% confidence. This score makes the confidence threshold project setting unusable.
 
 | Text |	Predicted intent |	Confidence score |
 |----|----|----|
@@ -243,7 +243,7 @@ curl --request POST \
 
 ## Address out-of-domain utterances
 
-Customers can use the newly updated recipe version `2024-08-01-preview` (previously `2024-06-01-preview`) if the model has poor AIQ on out-of-domain utterances. An example of this scenario with the default recipe can be like the following example where the model has three intents: `Sports`, `QueryWeather`, and `Alarm`. The test utterances are out-of-domain utterances and the model classifies them as `InDomain` with a relatively high confidence score.
+Customers can use the newly updated training configuration version `2024-08-01-preview` (previously `2024-06-01-preview`) if the model has poor quality on out-of-domain utterances. An example of this scenario with the default training configuration can be like the following example where the model has three intents: `Sports`, `QueryWeather`, and `Alarm`. The test utterances are out-of-domain utterances and the model classifies them as `InDomain` with a relatively high confidence score.
 
 | Text |	Predicted intent |	Confidence score |
 |----|----|----|
@@ -273,6 +273,6 @@ After the request is sent, you can track the progress of the training job in Lan
 
 Caveats:
 
-- The None score threshold for the app (confidence threshold below which `topIntent` is marked as `None`) when you use this recipe should be set to 0. This setting is used because this new recipe attributes a certain portion of the in-domain probabilities to out of domain so that the model isn't incorrectly overconfident about in-domain utterances. As a result, users might see slightly reduced confidence scores for in-domain utterances as compared to the prod recipe.
-- We don't recommend this recipe for apps with only two intents, such as `IntentA` and `None`, for example.
-- We don't recommend this recipe for apps with a low number of utterances per intent. We highly recommend a minimum of 25 utterances per intent.
+- The None score threshold for the app (confidence threshold below which `topIntent` is marked as `None`) when you use this training configuration should be set to 0. This setting is used because this new training configuration attributes a certain portion of the in-domain probabilities to out of domain so that the model isn't incorrectly overconfident about in-domain utterances. As a result, users might see slightly reduced confidence scores for in-domain utterances as compared to the prod training configuration.
+- We don't recommend this training configuration for apps with only two intents, such as `IntentA` and `None`, for example.
+- We don't recommend this training configuration for apps with a low number of utterances per intent. We highly recommend a minimum of 25 utterances per intent.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベストプラクティス記事の軽微な更新"
}
```

### Explanation
このコードの変更は、会話型言語理解サービスに関する「ベストプラクティス」ドキュメントの軽微な修正を示しています。主に、用語の統一と明確化が行われています。特に、「AIQ」と呼ばれるモデル品質の用語が、「モデル品質」に修正され、より理解しやすくなっています。また、「トレーニング設定」が「レシピ」の代わりに使用され、文中の説明が改善されています。これにより、ユーザーがトレーニング方法や評価基準を理解するのが容易になり、文章が全体的に洗練されています。全体で6行の追加と削除が行われており、内容は12行変更されています。この変更は、より明確で一貫性のある情報提供を目指すものです。

## articles/ai-studio/how-to/configure-private-link.md{#item-bbf93d}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,6 @@ You get several hub default resources in your resource group. You need to config
 - Disable public network access of hub default resources such as Azure Storage, Azure Key Vault, and Azure Container Registry.
 - Establish private endpoint connection to hub default resources. You need to have both a blob and file private endpoint for the default storage account.
 - [Managed identity configurations](#managed-identity-configuration) to allow hubs access your storage account if it's private.
-- Azure AI Search should be public.
 
 
 ## Prerequisites
@@ -280,7 +279,6 @@ To check AI-PROJECT-GUID, go to the Azure portal, select your project, settings,
 
 ## Limitations
 
-* Private Azure AI Services and Azure AI Search aren't supported.
 * The "Add your data" feature in the Azure AI Studio playground doesn't support private storage account.
 * You might encounter problems trying to access the private endpoint for your hub if you're using Mozilla Firefox. This problem might be related to DNS over HTTPS in Mozilla Firefox. We recommend using Microsoft Edge or Google Chrome.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンク設定に関する軽微な修正"
}
```

### Explanation
このコードの変更は、プライベートリンクの設定に関するドキュメントの軽微な修正を表しています。具体的には、リストから「Azure AI Searchは公開であるべきです」という文と、「プライベートAzure AIサービスとAzure AI Searchはサポートされていない。」という文が削除されました。これにより、ドキュメントがより簡潔になり、不要な情報が除去されたことで、ユーザーが理解しやすい内容になっています。変更は合計で2行の削除と2行の変更を含んでおり、情報の整合性を保ちながらも明瞭性の向上が図られています。

## articles/ai-studio/how-to/create-azure-ai-resource.md{#item-998abe}

<details>
<summary>Diff</summary>
````diff
@@ -12,13 +12,14 @@ ms.date: 5/21/2024
 ms.reviewer: deeikele
 ms.author: larryfr
 author: Blackmist
+# Customer Intent: As an admin, I need to create and manage an Azure AI Studio hub so that my team can use it to create projects for collaboration.
 ---
 
 # How to create and manage an Azure AI Studio hub
 
 In AI Studio, hubs provide the environment for a team to collaborate and organize work, and help you as a team lead or IT admin centrally set up security settings and govern usage and spend. You can create and manage a hub from the Azure portal or from the AI Studio. 
 
-In this article, you learn how to create and manage a hub in AI Studio with the default settings so you can get started quickly. Do you need to customize security or the dependent resources of your hub? Then use [Azure Portal](create-secure-ai-hub.md) or [template options](create-azure-ai-hub-template.md). 
+In this article, you learn how to create and manage a hub in AI Studio with the default settings so you can get started quickly. Do you need to customize security or the dependent resources of your hub? Then use [Azure portal](create-secure-ai-hub.md) or [template options](create-azure-ai-hub-template.md). 
 
 > [!TIP]
 > If you'd like to create your Azure AI Studio hub using a template, see the articles on using [Bicep](create-azure-ai-hub-template.md) or [Terraform](create-hub-terraform.md).
@@ -105,7 +106,7 @@ For hubs that use CMK encryption mode, you can update the encryption key to a ne
 
 To use custom environments for Prompt Flow, you're required to configure an Azure Container Registry for your hub. To use Azure Application Insights for Prompt Flow deployments, a configured Azure Application Insights resource is required for your hub. Updating the workspace-attached Azure Container Registry or ApplicationInsights resources may break lineage of previous jobs, deployed inference endpoints, or your ability to rerun earlier jobs in the workspace. 
 
-You can use the Azure Portal, Azure SDK/CLI options, or the infrastructure-as-code templates to update both Azure Application Insights and Azure Container Registry for the hub.
+You can use the Azure portal, Azure SDK/CLI options, or the infrastructure-as-code templates to update both Azure Application Insights and Azure Container Registry for the hub.
 
 # [Azure portal](#tab/portal)
 
@@ -142,7 +143,23 @@ az ml workspace update -n "myexamplehub" -g "{MY_RESOURCE_GROUP}" -a "APPLICATIO
 ```
 ---
 
-## Next steps
+## Delete an Azure AI Studio hub
+
+To delete a hub, use the [Azure portal](https://portal.azure.com). To quickly get to the Azure portal from the Azure AI Studio, go to the **Hub overview** for your hub and then select **Manage in Azure portal**.
+
+:::image type="content" source="../media/how-to/hubs/manage-hub-azure-portal.png" alt-text="Screenshot of the manage in Azure portal link in Azure AI Studio.":::
+
+From the portal page for your hub, select **Overview** along the left side of the page and then select **Delete** from the top of the page.
+
+:::image type="content" source="../media/how-to/hubs/delete-hub-button.png" alt-text="Screenshot of the delete button for the Azure AI Studio hub in the Azure portal.":::
+
+You can also find your hub in the Azure portal by entering the hub name in the search field at the top of the Azure portal. Select the hub from the **Resources** list to navigate to the **Overview** page for the hub.
+
+:::image type="content" source="../media/how-to/hubs/search-in-portal.png" alt-text="Screenshot of using the search field in the Azure portal to find a hub.":::
+
+
+
+## Related content
 
 - [Create a project](create-projects.md)
 - [Learn more about Azure AI Studio](../what-is-ai-studio.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioハブの管理に関する情報の追加と修正"
}
```

### Explanation
このコードの変更は、Azure AI Studioのリソース作成に関するドキュメントの更新を示しています。主な変更点は、Azure AI Studioハブの削除方法に関する新しいセクションの追加です。この新しいセクションには、ハブを削除する手順やAzureポータルを使用する方法が詳述されており、特にユーザーがハブを管理する際の便利な情報が提供されています。

さらに、いくつかの表現が修正され、「Azure Portal」という表記が「Azure portal」に統一されています。また、カスタマーインテントの説明が追加され、管理者としてのニーズが反映されています。全体として、20の追加、3の削除、23の変更が行われ、ユーザーがより簡潔で理解しやすい情報を得られるように文書が改善されています。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -214,12 +214,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
 > [!WARNING]
-> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -482,7 +482,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -580,7 +580,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -606,7 +606,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -775,7 +775,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1088,7 +1088,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Jais doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Jais models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1165,14 +1165,14 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Jais, see the following examples and tutorials:
+For more examples of how to use Jais models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 
-## Cost and quota considerations for Jais family of models deployed as serverless API endpoints
+## Cost and quota considerations for Jais models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -1189,4 +1189,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JaisモデルのJSON出力フォーマットに関する情報の修正と詳細の追加"
}
```

### Explanation
このコードの変更は、Jaisモデルのデプロイ方法に関するドキュメントの更新を反映しています。主な変更点は、JSON出力フォーマットに関連する注意喚起の文言が改善され、「JaisではJSON出力フォーマットをサポートしていない」という表現が「JaisモデルではJSON出力フォーマットをサポートしていない」と修正されています。これにより、モデルの使用に関する明確さが向上しています。

さらに、10行の追加と10行の削除が行われ、全体で20行の変更が加えられています。具体的には、SamplesやTutorialsの見出しにおいて、Jaisモデルの使用方法に関する具体的な説明が追加されており、ユーザーが情報をより容易に取得できるように整備されています。また、最後のセクションにおいて、関連リソースへのリンクも整理され、情報の一貫性が強化されています。これにより、ユーザーはJaisモデルのデプロイや使用に関する情報をよりスムーズに利用できるようになります。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -268,12 +268,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
 > [!WARNING]
-> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -610,7 +610,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -765,7 +765,7 @@ For deployment to a self-hosted managed compute, you must have enough quota in y
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -791,7 +791,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -973,7 +973,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1348,7 +1348,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Meta Llama doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Meta Llama models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1441,7 +1441,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Meta Llama, see the following examples and tutorials:
+For more examples of how to use Meta Llama models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                             |
 |-------------------------------------------|-------------------|------------------------------------------------------------------- |
@@ -1453,7 +1453,7 @@ For more examples of how to use Meta Llama, see the following examples and tutor
 | LangChain                                 | Python            | [Link](https://aka.ms/meta-llama-3.1-405B-instruct-langchain)      |
 | LiteLLM                                   | Python            | [Link](https://aka.ms/meta-llama-3.1-405B-instruct-litellm)        | 
 
-## Cost and quota considerations for Meta Llama family of models deployed as serverless API endpoints
+## Cost and quota considerations for Meta Llama models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -1463,7 +1463,7 @@ Each time a project subscribes to a given offer from the Azure Marketplace, a ne
 
 For more information on how to track costs, see [Monitor costs for models offered through the Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
 
-## Cost and quota considerations for Meta Llama family of models deployed to managed compute
+## Cost and quota considerations for Meta Llama models deployed to managed compute
 
 Meta Llama models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Meta Llamaモデルに関する情報の修正と更新"
}
```

### Explanation
このコードの変更は、Meta Llamaモデルのデプロイに関するドキュメントの更新を示しています。主な変更点は、JSON出力フォーマットに関連する警告表現を改善し、「Meta LlamaがJSON出力フォーマットをサポートしていない」という文言を「Meta LlamaモデルではJSON出力フォーマットをサポートしていない」と修正したことです。この修正により、表現が一貫性を持ち、ユーザーにとって理解しやすくなっています。

また、ドキュメント全体にわたって、10行の追加と10行の削除があり、合計で20行の変更が行われています。特に、モデルの使用に関する手引きやサンプルの説明において、Meta Llamaモデルの使用方法が明確にされており、ユーザーがモデルを適切に利用できるように配慮されています。さらに、関連するリソースへのリンクも整理され、情報の参照が容易になっているため、ユーザーが必要な情報にアクセスしやすくなっています。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral Nemo chat model with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/08/2024
+ms.date: 09/13/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -222,7 +222,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
@@ -242,7 +242,7 @@ response = client.complete(
                       " the following format: { ""answer"": ""response"" }."),
         UserMessage(content="How many languages are in the world?"),
     ],
-    response_format=ChatCompletionsResponseFormatJSON()
+    response_format={ "type": ChatCompletionsResponseFormatJSON() }
 )
 ```
 
@@ -962,7 +962,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -988,7 +988,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -2010,7 +2010,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Mistral, see the following examples and tutorials:
+For more examples of how to use Mistral models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -2024,7 +2024,7 @@ For more examples of how to use Mistral, see the following examples and tutorial
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral family of models deployed as serverless API endpoints
+## Cost and quota considerations for Mistral models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -2041,4 +2041,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistral Nemoモデルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Mistral Nemoモデルの使用に関するドキュメントの更新を示しています。主な変更点は、日付の更新、JSON出力フォーマットを指定する際の表現の改善、ならびに文体の一貫性向上が含まれています。具体的には、日付が「08/08/2024」から「09/13/2024」に修正され、`response_format`を指定するコードが修正されています。これにより、呼び出し時に必要なフォーマットが明確になり、正確性が増しています。

加えて、NuGetの表記が「Nuget」から「NuGet」に変更され、専門用語の一貫性が保たれています。他にも、モデルに関連する情報が明確になり、特に「Mistralモデル」との表現が統一されました。これにより、ユーザーはモデルの使い方や関連情報をより容易に理解できるようになっています。全体として、8行の追加と8行の削除が行われ、合計で16行の変更が加えられています。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral-7B and Mixtral chat models with Azure AI S
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/08/2024
+ms.date: 09/13/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -63,8 +63,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
-* Pprecise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Precise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -270,12 +270,12 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
 > [!WARNING]
-> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -352,8 +352,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
-* Pprecise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Precise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -576,7 +576,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -658,8 +658,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
-* Pprecise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Precise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -689,7 +689,7 @@ For deployment to a self-hosted managed compute, you must have enough quota in y
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -715,7 +715,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -897,7 +897,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -976,8 +976,8 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling; along with the constrained output mode implemented on la Plateforme, this enables application development and tech stack modernization at scale
-* Pprecise information recall from large documents, due to its 64K tokens context window
+* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Precise information recall from large documents, due to its 64K tokens context window
 
 
 The following models are available:
@@ -1230,7 +1230,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Mistral doesn't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1279,7 +1279,7 @@ The following extra parameters can be passed to Mistral-7B and Mixtral chat mode
 
 ## More inference examples
 
-For more examples of how to use Mistral, see the following examples and tutorials:
+For more examples of how to use Mistral models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -1293,7 +1293,7 @@ For more examples of how to use Mistral, see the following examples and tutorial
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral family of models deployed to managed compute
+## Cost and quota considerations for Mistral models deployed to managed compute
 
 Mistral models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
@@ -1306,4 +1306,4 @@ It is a good practice to start with a low number of instances and scale up as ne
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルに関する情報の更新"
}
```

### Explanation
このコードの変更は、MistralおよびMixtralチャットモデルのデプロイに関するドキュメントのアップデートを示しています。主な変更点には、日付の修正（「08/08/2024」から「09/13/2024」への変更）、および説明文のリフレーズが含まれています。特に、Mixtralモデルの特性に関する記載が改善されており、機能呼び出し能力の説明がより明確になっています。

さらに、ドキュメント内で「MistralがJSON出力フォーマットをサポートしていない」という警告の一貫性が強調され、表現が改善されました。`response_format`の指定に関するコードも明確化され、構文が一貫していることが確認されています。これにより、ユーザーはモデルの使用方法をより直感的に理解できるようになっています。

全体として、この更新には19行の追加と19行の削除があり、合計で38行の変更が行われています。これにより、Mistralモデルに関する情報が最新の状態に保たれ、ユーザーにとっての利便性が向上しています。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Mistral premium chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/08/2024
+ms.date: 09/13/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -252,7 +252,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
@@ -272,7 +272,7 @@ response = client.complete(
                       " the following format: { ""answer"": ""response"" }."),
         UserMessage(content="How many languages are in the world?"),
     ],
-    response_format=ChatCompletionsResponseFormatJSON()
+    response_format={ "type": ChatCompletionsResponseFormatJSON() }
 )
 ```
 
@@ -1052,7 +1052,7 @@ Deployment to a serverless API endpoint doesn't require quota from your subscrip
 
 ### The inference package installed
 
-You can consume predictions from this model by using the `Azure.AI.Inference` package from [Nuget](https://www.nuget.org/). To install this package, you need the following prerequisites:
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
 
 * The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
 * Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
@@ -1078,7 +1078,7 @@ using Azure.Identity;
 using Azure.AI.Inference;
 ```
 
-This example also use the following namespaces but you may not always need them:
+This example also uses the following namespaces but you may not always need them:
 
 
 ```csharp
@@ -2130,7 +2130,7 @@ The following example shows how to handle events when the model detects harmful
 
 ## More inference examples
 
-For more examples of how to use Mistral, see the following examples and tutorials:
+For more examples of how to use Mistral models, see the following examples and tutorials:
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
@@ -2144,7 +2144,7 @@ For more examples of how to use Mistral, see the following examples and tutorial
 | LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
 
 
-## Cost and quota considerations for Mistral family of models deployed as serverless API endpoints
+## Cost and quota considerations for Mistral models deployed as serverless API endpoints
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
@@ -2161,4 +2161,4 @@ For more information on how to track costs, see [Monitor costs for models offere
 * [Deploy models as serverless APIs](deploy-models-serverless.md)
 * [Consume serverless API endpoints from a different Azure AI Studio project or hub](deploy-models-serverless-connect.md)
 * [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
-* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
\ No newline at end of file
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralチャットモデルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Mistralプレミアムチャットモデルに関するドキュメントの更新を示しています。主な修正点には、文書の日付を「08/08/2024」から「09/13/2024」に変更したことが含まれます。また、`response_format`を指定する方法が変更され、より明確な構文が使用されています。具体的には、`ChatCompletionsResponseFormatText()`や`ChatCompletionsResponseFormatJSON()`の指定がオブジェクト形式に変更されています。

さらに、NuGetパッケージの表記が「Nuget」から「NuGet」に修正され、文書内での用語の一貫性が向上しています。他にも、Mistralモデルに関連する情報がより明確に表現されており、ユーザーがモデルに関する情報を簡単に理解できるようになっています。

全体として、8行の追加と8行の削除が行われており、合計で16行の変更がなされています。この更新によって、Mistralモデルに関する情報が最新の状態に保たれ、ユーザー体験が向上しています。

## articles/ai-studio/how-to/deploy-models-phi-3-5-moe.md{#item-9af6ea}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3.5 MoE chat model with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/19/2024
+ms.date: 09/13/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -232,7 +232,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3.5 MoEモデルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Phi-3.5 MoEチャットモデルに関するドキュメントの更新を示しています。主な変更点は、文書の日付を「08/19/2024」から「09/13/2024」に変更したことです。また、`response_format`の指定方法が改善され、従来の形式からオブジェクト形式に更新されています。これにより、より明確で一貫性のあるコードが提供されています。

合計で2行の追加と2行の削除が行われ、全体で4行の変更があります。この更新により、Phi-3.5 MoEモデルに関する情報が最新化され、利用者にとっての利便性が向上しています。

## articles/ai-studio/how-to/deploy-models-phi-3-vision.md{#item-bd5aae}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3 chat model with vision with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/19/2024
+ms.date: 09/13/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -228,7 +228,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3ビジョンモデルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Phi-3ビジョンチャットモデルに関するドキュメントの更新を示しています。主な修正点には、文書の日付を「08/19/2024」から「09/13/2024」に更新したことが含まれます。また、`response_format`の指定方法が変更され、従来の形式からより明確なオブジェクト形式に改善されています。

合計で2行の追加と2行の削除が行われており、変更全体で4行が修正されています。この更新により、Phi-3ビジョンモデルに関する情報が最新のものとなり、ユーザーの理解を助ける内容になっています。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Phi-3 family chat models with Azure AI Studio.
 ms.service: azure-ai-studio
 manager: scottpolly
 ms.topic: how-to
-ms.date: 08/19/2024
+ms.date: 09/13/2024
 ms.reviewer: kritifaujdar
 reviewer: fkriti
 ms.author: mopeakande
@@ -269,7 +269,7 @@ response = client.complete(
     stop=["<|endoftext|>"],
     temperature=0,
     top_p=1,
-    response_format=ChatCompletionsResponseFormatText(),
+    response_format={ "type": ChatCompletionsResponseFormatText() },
 )
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3ファミリーチャットモデルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Phi-3ファミリーチャットモデルに関するドキュメントの更新を示しています。主な変更点は、文書の日付を「08/19/2024」から「09/13/2024」に変更したことです。また、`response_format`の定義方法が従来の形式から明確なオブジェクト形式に変更され、コードの可読性と一貫性が向上しています。

合計で2行の追加と2行の削除があり、全体で4行の変更が実施されています。これにより、Phi-3ファミリーチャットモデルに関する情報が最新のものとなり、利用者にとって役立つ内容に更新されています。

## articles/ai-studio/how-to/fine-tune-model-llama.md{#item-2a42d8}

<details>
<summary>Diff</summary>
````diff
@@ -230,7 +230,7 @@ To fine-tune a Llama 2 model in an existing Azure AI Studio project, follow thes
 
     :::image type="content" source="../media/how-to/fine-tune/llama/llama-pay-as-you-go-overview.png" alt-text="Screenshot of pay-as-you-go marketplace overview." lightbox="../media/how-to/fine-tune/llama/llama-pay-as-you-go-overview.png":::
 
-1. Choose a base model to fine-tune and select **Confirm**. Your choice influences both the performance and [the cost of your model](./deploy-models-llama.md#cost-and-quota-considerations-for-meta-llama-family-of-models-deployed-as-serverless-api-endpoints).
+1. Choose a base model to fine-tune and select **Confirm**. Your choice influences both the performance and [the cost of your model](./deploy-models-llama.md#cost-and-quota-considerations-for-meta-llama-models-deployed-as-serverless-api-endpoints).
 
     :::image type="content" source="../media/how-to/fine-tune/llama/fine-tune-select-model.png" alt-text="Screenshot of option to select a model to fine-tune." lightbox="../media/how-to/fine-tune/llama/fine-tune-select-model.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Llamaモデルのファインチューニング手順の修正"
}
```

### Explanation
このコードの変更は、Llamaモデルのファインチューニングに関する手順の文書の更新を表しています。具体的には、手順の1項目において、「Meta Llamaファミリーのモデル」を「Meta Llamaモデル」に修正しました。この変更は、モデルの名称の一貫性を保つことを目的としています。

変更内容は、合計で1行の追加と1行の削除があり、全体で2行の修正が行われています。このような修正により、ユーザーが混乱することなく、正確な情報をもとに作業を進められるようになります。

## articles/ai-studio/media/how-to/hubs/delete-hub-button.png{#item-92c030}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ハブ削除ボタンの画像追加"
}
```

### Explanation
このコードの変更は、「delete-hub-button.png」という新しい画像ファイルの追加を示しています。この画像は、AIスタジオ内のハブに関連する操作において、ハブを削除する際のボタンの視覚的な表現を提供するものです。

具体的な変更点は0行の追加や削除はありませんが、新たに画像ファイルが追加されたことにより、ユーザーが手順を理解しやすくなることが期待されます。この新しいメディアコンテンツは、ドキュメントの質を向上させ、より効果的なユーザー体験を提供します。

## articles/ai-studio/media/how-to/hubs/manage-hub-azure-portal.png{#item-8f34ee}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azureポータルでのハブ管理に関する画像追加"
}
```

### Explanation
このコードの変更は、「manage-hub-azure-portal.png」という新しい画像ファイルの追加を示しています。この画像は、Azureポータルにおけるハブの管理手順を視覚的にサポートするもので、ユーザーが操作を理解しやすくするためのツールとして機能します。

具体的には、追加された画像は、関連する手順の説明を補完する役割を果たすことが期待されます。実際のコード変更は0行の追加や削除ですが、新しいメディアコンテンツにより、ドキュメントの全体的な品質が向上し、ユーザーにとってより効果的な情報提供が可能になります。

## articles/ai-studio/media/how-to/hubs/search-in-portal.png{#item-44ef96}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ポータル内検索に関する画像追加"
}
```

### Explanation
このコードの変更は、「search-in-portal.png」という新しい画像ファイルの追加を示しています。この画像は、ポータル内での検索手順を視覚的に説明するために用いられ、ユーザーの操作理解を助けることを目的としています。

変更内容は具体的には0行の追加や削除がないものの、新たに追加されたメディアは、関連するドキュメントや手順の理解を容易にする重要な要素となります。結果として、ユーザーはポータルの検索機能を効果的に利用できるようになり、全体の操作性の向上が期待されます。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -51,14 +51,14 @@ items:
       href: concepts/ai-resources.md
     - name: Create your first hub
       href: how-to/create-azure-ai-resource.md
+    - name: Create a hub using the Azure Machine Learning SDK and CLI
+      href: how-to/develop/create-hub-project-sdk.md
     - name: Create a hub with custom security
       items:
       - name: Create a hub in the Azure portal
         href: how-to/create-secure-ai-hub.md
       - name: Create a hub from template
         href: how-to/create-azure-ai-hub-template.md
-      - name: Create a hub using the Azure Machine Learning SDK and CLI
-        href: how-to/develop/create-hub-project-sdk.md
         displayName: code
       - name: Create a hub using Terraform
         href: how-to/create-hub-terraform.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルの更新：ハブ作成手順の整理"
}
```

### Explanation
このコードの変更は、「toc.yml」というファイルの修正を示しています。具体的には、ハブの作成に関連する手順の項目を追加したり削除したりして、内容を整理しています。

変更点の概要としては、2つの新しい項目が追加され、同時に2つの項目が削除されています。具体的には、「Azure Machine Learning SDKとCLIを使用してハブを作成する」という項目が削除され、その代わりに「Azure Machine Learning SDKとCLIを使用してハブを作成する」という新しい項目が追加されています。この修正により、ユーザーがハブを作成するための手順がより明確になり、正確で一貫性のある情報提供が行われます。

結果として、TOC（テーブルオブコンテンツ）ファイルの整理が進み、ユーザーは必要な情報に迅速にアクセスできるようになります。


