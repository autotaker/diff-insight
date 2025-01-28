---
date: '2025-01-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9cc44af...MicrosoftDocs:2067774
summary: このコード変更では、ドキュメントの微調整を通じて役割、リダイレクトURL、クラス名の明確化と修正が行われました。新機能や重大な変更はなく、利用者にとっての利便性と正確性が向上しています。具体的には、既存リソースの役割の指示を明確にし、リダイレクトURLを修正し、Azure
  AIリソースに関する注意点を追加し、Azure認証のクラス名を変更しました。これらの修正は細かなものですが、ユーザーの体験を向上させるために重要です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9cc44af...MicrosoftDocs:2067774){target="_blank"}

# Highlights
このコード変更では、ドキュメントの微調整を通じていくつかの役割とリダイレクトURL、クラス名の明確化と修正が行われました。新機能や重大な変更は含まれていませんが、利用者にとっての利便性と正確性が向上しています。

## New features
特に新機能は追加されていません。

## Breaking changes
重大な変更はありません。

## Other updates
1. 既存リソースの使用における役割の指示の明確化。
2. リダイレクト設定のURL修正。
3. Azure AIリソースの更新に関する注意点の追加。
4. Azure認証クラス名の変更。

# Insights
このドキュメントの更新は、主にユーザビリティの向上を目指しています。具体的に見ていくと、まず、既存リソースを用いる際の明確な役割の指定がなされ、「ストレージブロブデータ寄稿者」役割を持つべきであることが明確化されました。これは、役割の誤解によるアクセス権の問題を未然に防ぐためです。

次に、リダイレクトURLの微調整ですが、これはユーザーが必要な時に正しい情報に迅速にアクセスできるようにするための重要な修正です。正しいURLを使うことで、ユーザーは正確なガイダンスを得ることができます。

また、Azure AIリソースの注意事項に関する更新は、多くのユーザーがコンポーネントの管理を誤ることを防ぎます。特にリソースをAzure AI Foundryに関連付けた後、リソースを分離できないことが強調されています。

最後に、Azure認証クラス名の変更は、技術的な整合性を保つためのものであり、ユーザーがエラーなくコードを実行できることを保証します。この変更により、Python及びJavaScriptのコードスニペットで使用されるクラス名が最新のライブラリと一致し、他のプログラムコンポーネントと調和することになります。

これらの修正は、一見小さく思えるかもしれませんが、ユーザーの体験を向上させ、技術的な誤りやトラブルを防ぐために非常に重要です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-pre-existing-resource.md](#item-d11f5d) | minor update | 既存リソースを使用する際の役割の指示を明確化 | modified | 1 | 1 | 2 | 
| [.openpublishing.redirection.ai-studio.json](#item-c75c21) | minor update | リダイレクトURLの修正 | modified | 1 | 1 | 2 | 
| [create-azure-ai-resource.md](#item-998abe) | minor update | Azure AIリソースの更新に関する注意事項を追加 | modified | 1 | 1 | 2 | 
| [reference-model-inference-api.md](#item-9fe240) | minor update | Azure認証クラスの名称変更 | modified | 4 | 4 | 8 | 


# Modified Contents
## articles/ai-services/language-service/custom-named-entity-recognition/includes/use-pre-existing-resource.md{#item-d11f5d}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ Make sure to enable **Custom text classification / Custom Named Entity Recogniti
 5. Select **Apply**.
 
 >[!Important]
-> * Make sure that your **Language resource** has **storage blob data contributor** role assigned on the storage account you are connecting.
+> Make sure that the user making changes has **storage blob data contributor** role assigned for them.
 
 ### Add required roles
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "既存リソースを使用する際の役割の指示を明確化"
}
```

### Explanation
この変更は、ドキュメントの指示を微調整するもので、既存のリソースを使用する際に必要な役割に関する情報を明確にするものです。具体的には、データストレージアカウントに接続する際に、変更を加えるユーザーが「ストレージブロブデータ寄稿者」役割を持っているべきである旨の記述に修正が加えられました。この修正は、ユーザーが必要な権限を正確に理解し、適切に設定できるよう助けることを目的としています。変更箇所は、元の「Language resource」という表現を「変更を加えるユーザー」に変更することで、より具体的な役割の設定に焦点を当てています。

## articles/ai-studio/.openpublishing.redirection.ai-studio.json{#item-c75c21}

<details>
<summary>Diff</summary>
````diff
@@ -207,7 +207,7 @@
           },
           {
             "source_path_from_root": "/articles/ai-studio/ai-services/how-to/content-safety.md",
-            "redirect_url": "/azure/ai-foundry/model-inference/how-to/configure-content-safety",
+            "redirect_url": "/azure/ai-foundry/model-inference/how-to/configure-content-filters",
             "redirect_document_id": false
           },
           {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リダイレクトURLの修正"
}
```

### Explanation
この変更は、AIスタジオの関連ドキュメントにおけるリダイレクト設定の微調整を示しています。具体的には、ソースパス「/articles/ai-studio/ai-services/how-to/content-safety.md」に関連するリダイレクトURLが更新されました。以前のリダイレクトURL「/azure/ai-foundry/model-inference/how-to/configure-content-safety」は、「/azure/ai-foundry/model-inference/how-to/configure-content-filters」に修正されました。この変更により、ユーザーが正しい情報にアクセスできるようにURLが調整されており、コンテンツの一貫性と正確性が向上しています。

## articles/ai-studio/how-to/create-azure-ai-resource.md{#item-998abe}

<details>
<summary>Diff</summary>
````diff
@@ -111,7 +111,7 @@ For hubs that use CMK encryption mode, you can update the encryption key to a ne
 
 ### Update Azure Application Insights and Azure Container Registry
 
-To use custom environments for Prompt Flow, you're required to configure an Azure Container Registry for your hub. To use Azure Application Insights for Prompt Flow deployments, a configured Azure Application Insights resource is required for your hub. Updating the workspace-attached Azure Container Registry or ApplicationInsights resources may break lineage of previous jobs, deployed inference endpoints, or your ability to rerun earlier jobs in the workspace. 
+To use custom environments for Prompt Flow, you're required to configure an Azure Container Registry for your hub. To use Azure Application Insights for Prompt Flow deployments, a configured Azure Application Insights resource is required for your hub. Updating the workspace-attached Azure Container Registry or Application Insights resources may break lineage of previous jobs, deployed inference endpoints, or your ability to rerun earlier jobs in the workspace. After association with an Azure AI Foundry hub, Azure Container Registry and Application Insights resources cannot be disassociated (set to null).
 
 You can use the Azure portal, Azure SDK/CLI options, or the infrastructure-as-code templates to update both Azure Application Insights and Azure Container Registry for the hub.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AIリソースの更新に関する注意事項を追加"
}
```

### Explanation
この変更は、Azure AIリソースの作成に関するドキュメントにおいて、更新時の注意事項を追加するものです。具体的に、Azure Container RegistryおよびAzure Application Insightsリソースの更新に際して、これらのリソースがAzure AI Foundryハブに関連付けられた後は、リソースを切り離すことができない（nullに設定できない）ことが明記されました。この情報は、リソースの管理を行うユーザーが不必要なトラブルを避けるために重要です。変更された内容は、リソース更新による影響を理解して適切に操作を行うための助けとなることを目的としています。

## articles/ai-studio/reference/reference-model-inference-api.md{#item-9fe240}

<details>
<summary>Diff</summary>
````diff
@@ -115,11 +115,11 @@ If you are using an endpoint with support for Entra ID, you can create your clie
 ```python
 import os
 from azure.ai.inference import ChatCompletionsClient
-from azure.identity import AzureDefaultCredential
+from azure.identity import DefaultAzureCredential
 
 model = ChatCompletionsClient(
     endpoint=os.environ["AZUREAI_ENDPOINT_URL"],
-    credential=AzureDefaultCredential(),
+    credential=DefaultAzureCredential(),
 )
 ```
 
@@ -151,11 +151,11 @@ For endpoint with support for Microsoft Entra ID, you can create your client as
 ```javascript
 import ModelClient from "@azure-rest/ai-inference";
 import { isUnexpected } from "@azure-rest/ai-inference";
-import { AzureDefaultCredential } from "@azure/identity";
+import { DefaultAzureCredential } from "@azure/identity";
 
 const client = new ModelClient(
     process.env.AZUREAI_ENDPOINT_URL, 
-    new AzureDefaultCredential()
+    new DefaultAzureCredential()
 );
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure認証クラスの名称変更"
}
```

### Explanation
この変更は、Azure AIスタジオのモデル推論APIに関するリファレンスドキュメントで、認証クラスの名称変更に関する更新を含んでいます。具体的には、「AzureDefaultCredential」というクラス名が「DefaultAzureCredential」に変更されました。これは、PythonおよびJavaScriptのコードスニペットに影響を与えています。この更新により、最新のライブラリと整合性が取れ、ユーザーが正しいクラス名を使用して認証を行えるようになります。変更は、コードの正確性を保ち、ユーザーが正しい情報に基づいて作業を進められるようにするための重要な修正です。


