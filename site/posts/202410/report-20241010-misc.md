---
date: '2024-10-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eb045a9...MicrosoftDocs:7341d04
summary: この変更では、暗号化キーのポータルに関する記述の更新、Azure OpenAIモデルのクライアント設定情報の追加、モデルカタログの展開オプションの情報の追加、カスタムナビゲーションのGIFファイルの削除、TOCのセクション整理と名称変更が含まれています。新機能としては、Azure
  OpenAIモデルのクライアント設定が詳しく説明され、モデルカタログの展開オプションが新たに追加されました。一方、破壊的変更として「custom-navigation.gif」が削除され、これによりビジュアルガイドラインに影響が及ぶ可能性があります。その他の更新には、暗号化キーに関する記事の小規模修正やAI
  Studioの目次ファイルの整理があります。これらの変更は、ユーザーエクスペリエンスの向上を目指し、用語の正確性を高め、情報の整理を行っています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eb045a9...MicrosoftDocs:7341d04){target="_blank"}

# ハイライト

この変更では、暗号化キーのポータルに関する記述の更新、Azure OpenAIモデルのクライアント設定情報の追加、モデルカタログの展開オプションの情報の追加、カスタムナビゲーションのGIFファイルの削除、そしてTOCのセクション整理と名称変更が行われました。

## 新機能
- Azure OpenAIモデルのクライアント設定に関する詳細情報が追加されました。
- モデルカタログの展開オプションに新しいセクションが追加され、管理されたコンピュートとサーバーレスAPIの展開方法が説明されています。

## 破壊的変更
- `custom-navigation.gif`というメディアファイルが削除されました。これにより、ビジュアルガイドラインが影響を受ける可能性があります。

## その他の更新
- 「暗号化キーのポータル」記事が、小規模更新されました。「サーバー側暗号化」の表現が「サービス側暗号化」に変更され、関連箇所が修正されています。
- AI Studioの目次ファイルが整理され、「Infrastructure & security」セクションが「Security & Governance」に改名されました。

# インサイト

この更新では、ユーザーエクスペリエンスの向上を目指した様々な改善が行われています。まず、暗号化キーに関する記事の修正は、用語の正確性を高め、読者に誤解を与えないようにするためのものです。特に、Azure Key Vaultに関連する注意事項の更新は、セキュリティ関連のリスクを回避し、透明性を高めることを目的としています。

Azure OpenAIモデルに関する新機能の追加は、特に企業ユーザーにとって重要です。認証キーの設定方法が明示されたことで、開発者が迅速に設定を行い、AIモデルを確実に利用できるようになることが期待されます。この種の具体的な情報提供は、プロジェクトの効率に貢献します。

モデルカタログの更新により、ユーザーはより多くの展開オプションの中から適切なものを選択できるようになりました。また、Llamaファミリーの各モデルに関する詳細が追加されているため、ユーザーはモデルの特性に基づいた意思決定を行うことができます。

カスタムナビゲーションのGIFファイル削除は、コンテンツの再編成や新たなメディア導入の必要性を示していると考えられます。ユーザー体験に影響を与えるため、追加の補完が必要です。

最後に、AI StudioのTOC更新は、内容をより整理されたものにし、ユーザーが必要な情報にアクセスしやすくするための施策です。セキュリティとガバナンス関連の情報が明確に提供されているため、セキュリティ意識の高いユーザーにとっては有益です。

これらの更新は、全体としてユーザー指向の改善を反映しており、ユーザーがより効率的に文書を参照できるようになっただけでなく、セキュリティや機能性に関する理解が深まる内容となっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [encryption-keys-portal.md](#item-95428d) | minor update | 暗号化キーのポータルに関する最新情報の更新 | modified | 2 | 2 | 4 | 
| [llama-index.md](#item-613372) | new feature | Azure OpenAI モデルのクライアント設定に関する追加情報 | modified | 19 | 2 | 21 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログの展開オプションに関する情報の追加 | modified | 4 | 0 | 4 | 
| [custom-navigation.gif](#item-6371cb) | breaking change | カスタムナビゲーションの GIF ファイルの削除 | removed | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | セクションの整理と名称変更による TOC の更新 | modified | 29 | 29 | 58 | 


# Modified Contents
## articles/ai-studio/concepts/encryption-keys-portal.md{#item-95428d}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ The following data is stored on the managed resources.
 A new architecture for customer-managed key encryption with hubs is available in preview, which resolves the dependency on the managed resource group. In this new model, encrypted data is stored service-side on Microsoft-managed resources instead of in managed resources in your subscription. Metadata is stored in multitenant resources using document-level CMK encryption. An Azure AI Search instance is hosted on the Microsoft-side per customer, and for each hub. Due to its dedicated resource model, its Azure cost is charged in your subscription via the hub resource.
 
 > [!NOTE]
-> During this preview key rotation and user-assigned identity capabilities are not supported. Server-side encryption is currently not supported in reference to an Azure Key Vault for storing your encryption key that has public network access disabled.
+> During this preview key rotation and user-assigned identity capabilities are not supported. Service-side encryption is currently not supported in reference to an Azure Key Vault for storing your encryption key that has public network access disabled.
 
 ## Use customer-managed keys with Azure Key Vault
 
@@ -83,7 +83,7 @@ Customer-managed key encryption is configured via Azure portal in a similar way
 1. Create a new Azure resource in Azure portal.
 1. Under the encryption tab, select your encryption key.
 
-:::image type="content" source="../../machine-learning/media/concept-customer-managed-keys/cmk-service-side-encryption.png" alt-text="Screenshot of the encryption tab with the option for server side encryption selected." lightbox="../../machine-learning/media/concept-customer-managed-keys/cmk-service-side-encryption.png":::
+:::image type="content" source="../../machine-learning/media/concept-customer-managed-keys/cmk-service-side-encryption.png" alt-text="Screenshot of the encryption tab with the option for service side encryption selected." lightbox="../../machine-learning/media/concept-customer-managed-keys/cmk-service-side-encryption.png":::
 
 Alternatively, use infrastructure-as-code options for automation. Example Bicep templates for Azure AI Studio are available on the Azure Quickstart repo:
 1. [CMK encryption for hub](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aistudio-cmk).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キーのポータルに関する最新情報の更新"
}
```

### Explanation
このコードの差分は、「暗号化キーのポータル」に関するドキュメントにおける小規模な更新を示しています。主要な変更点は、サーバー側の暗号化に関する説明であり、従来の「サーバー側暗号化」という表現が「サービス側暗号化」に変更されています。この修正は、より正確な情報を提供するために行われました。

具体的には、プレビュー中のキー回転やユーザー指定のアイデンティティ機能がサポートされていないこと、また、Azure Key Vaultにおける公開ネットワークアクセスが無効な暗号化キーの保存に関するサーバー側暗号化の非サポートについての注意書きも更新されました。

この更新は、暗号化キーに関する情報とその使用方法に関する記事の整合性を高め、正確性を向上させることを目的としています。

## articles/ai-studio/how-to/develop/llama-index.md{#item-613372}

<details>
<summary>Diff</summary>
````diff
@@ -67,7 +67,7 @@ export AZURE_INFERENCE_ENDPOINT="<your-model-endpoint-goes-here>"
 export AZURE_INFERENCE_CREDENTIAL="<your-key-goes-here>"
 ```
 
-Once configured, create a client to connect to the endpoint:
+Once configured, create a client to connect to the endpoint. The parameter `model_name` in the constructor is not required for endpoints serving a single model, like serverless endpoints.
 
 ```python
 import os
@@ -80,7 +80,7 @@ llm = AzureAICompletionsModel(
 ```
 
 > [!TIP]
-> The parameter `model_name` in the constructor is not required for endpoints serving a single model, like serverless endpoints).
+> If your model is an OpenAI model deployed to Azure OpenAI service or AI services resource, configure the client as indicated at [Azure OpenAI models](#azure-openai-models).
 
 Alternatively, if your endpoint support Microsoft Entra ID, you can use the following code to create the client:
 
@@ -112,6 +112,23 @@ llm = AzureAICompletionsModel(
 )
 ```
 
+### Azure OpenAI models
+
+If you are using Azure OpenAI models with key-based authentication, you need to pass the authentication key in the header `api-key`, which is the one expected in the Azure OpenAI service and in Azure AI Services. This configuration is not required if you are using Microsoft Entra ID (formerly known as Azure AD). The following example shows how to configure the client:
+
+```python
+import os
+from llama_index.llms.azure_inference import AzureAICompletionsModel
+
+llm = AzureAICompletionsModel(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential="",
+    client_kwargs={"headers" : { "api-key": os.environ["AZURE_INFERENCE_CREDENTIAL"] } }
+)
+```
+
+Notice that `credentials` is still being passed with an empty value since it's a required parameter.
+
 ### Inference parameters
 
 You can configure how inference in performed for all the operations that are using this client by setting extra parameters. This helps avoid indicating them on each call you make to the model.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAI モデルのクライアント設定に関する追加情報"
}
```

### Explanation
このコードの差分は、「Llama Index」のドキュメントに新しい情報が追加されたことを示しています。主な変更点は、Azure OpenAIモデルを使用する際のクライアント設定に関する詳細が新たに加わったことです。

具体的には、Azure OpenAIサービスやAzure AIサービスリソースにデプロイされているOpenAIモデルを使用する場合、`api-key`というヘッダーで認証キーを渡す必要があることが明示されています。これにより、ユーザーはモデルの利用時に必要な設定を理解しやすくなります。また、Microsoft Entra ID（以前のAzure AD）を使用する場合には、この設定が不要であることも説明されています。

さらに、新しいコード例が追加され、`AzureAICompletionsModel`のインスタンスを作成する際に、APIキーをヘッダーにセットする方法が示されています。これにより、ユーザーは新たに加えられた設定情報に従って、より簡単にAzure OpenAIモデルを利用できるようになります。全体として、これらの変更は情報の追加により機能性を向上させており、ユーザー体験を改善することを目的としています。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -53,6 +53,8 @@ For more information on Azure OpenAI models, see [What is Azure OpenAI Service?]
 The model catalog offers two distinct ways to deploy models for your use: managed compute and serverless APIs.
 
 The deployment options and features available for each model vary, as described in the following tables. [Learn more about data processing with the deployment options]( concept-data-privacy.md).
+
+### Capabilities of model deployment options
 <!-- docutune:disable -->
 
 Features | Managed compute | Serverless API (pay-as-you-go)
@@ -62,6 +64,8 @@ API authentication | Keys and Microsoft Entra authentication. | Keys only.
 Content safety | Use Azure AI Content Safety service APIs. | Azure AI Content Safety filters are available integrated with inference APIs. Azure AI Content Safety filters are billed separately.
 Network isolation | [Configure managed networks for Azure AI Studio hubs](configure-managed-network.md).  | Managed compute follow your hub's public network access (PNA) flag setting. For more information, see the [Network isolation for models deployed via Serverless APIs](#network-isolation-for-models-deployed-via-serverless-apis) section later in this article.
 
+### Available models for supported deployment options
+
 Model | Managed compute | Serverless API (pay-as-you-go)
 --|--|--
 Llama family models | Llama-2-7b <br> Llama-2-7b-chat <br> Llama-2-13b <br> Llama-2-13b-chat <br> Llama-2-70b <br> Llama-2-70b-chat <br> Llama-3-8B-Instruct <br> Llama-3-70B-Instruct <br> Llama-3-8B <br> Llama-3-70B | Llama-3-70B-Instruct <br> Llama-3-8B-Instruct <br> Llama-2-7b <br> Llama-2-7b-chat <br> Llama-2-13b <br> Llama-2-13b-chat <br> Llama-2-70b <br> Llama-2-70b-chat
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルカタログの展開オプションに関する情報の追加"
}
```

### Explanation
このコードの差分は、「モデルカタログの概要」に関するドキュメントにおいて、小規模な更新が行われたことを示しています。主な変更として、モデルの展開オプションに関する新しいセクションが追加され、これにより管理されたコンピュートとサーバーレスAPIという異なるモデルの展開方法の能力が明確に説明されています。

具体的には、各モデルの展開オプションや特徴に関する表が導入され、モデルごとに使用できる機能やAPI認証方法が示されています。また、サーバーレスAPIにおけるネットワークアイソレーションや、保護されたコンテンツの利用に関する情報も追加されています。さらに、サポートされている展開オプションに基づいたモデルのリストが提供され、Llamaファミリーの各モデルが管理されたコンピュートとサーバーレスAPIのどちらで利用可能かが示されています。

この更新は、ユーザーがモデルを展開する際の選択肢とそれぞれの特徴をより理解できるようにすることを目的としています。全体として、情報の明確化と利便性の向上が図られており、リーダビリティが向上しています。

## articles/ai-studio/media/explore/custom-navigation.gif{#item-6371cb}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムナビゲーションの GIF ファイルの削除"
}
```

### Explanation
このコードの差分は、カスタムナビゲーションに関連するGIFファイルが削除されたことを示しています。具体的には、`custom-navigation.gif`というメディアファイルがドキュメントから取り除かれました。この変更により、ユーザーはこのGIFを参照できなくなり、関連するビジュアルガイドラインや説明が影響を受ける可能性があります。

通常、このようなファイルの削除は、更新された情報や新しいメディアの導入に伴うものであることが多いですが、ユーザーにとっては視覚的な参考がなくなることを意味します。そのため、もしこのGIFが重要なコンテンツを提供していた場合、他の素材や情報で補完する必要があります。全体として、これはユーザーエクスペリエンスに影響を与える可能性がある重要な変更です。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -304,36 +304,36 @@ items:
       href: how-to/quota.md
     - name: Increase rate limit
       href: how-to/autoscale.md
-  - name: Infrastructure & security
+- name: Security & Governance
+  items:
+  - name: Identity & access management
     items:
-    - name: Identity & access management
-      items:
-      - name: Role-based access control in Azure AI Studio
-        href: concepts/rbac-ai-studio.md
-    - name: Network security
-      items:
-      - name: Configure managed network
-        href: how-to/configure-managed-network.md
-      - name: Configure private link
-        href: how-to/configure-private-link.md
-      - name: Configure custom DNS
-        href: /azure/machine-learning/how-to-custom-dns?context=/azure/ai-studio/context/context
-      - name: Secure playground chat
-        href: how-to/secure-data-playground.md
-      - name: Troubleshoot secure project connectivity
-        href: how-to/troubleshoot-secure-connection-project.md
-    - name: Data protection & encryption
-      items:
-      - name: Configure customer-managed keys
-        href: concepts/encryption-keys-portal.md
-      - name: Rotate keys
-        href: ../ai-services/rotate-keys.md?context=/azure/ai-studio/context/context
-    - name: Vulnerability management
-      href: concepts/vulnerability-management.md
-    - name: Disaster recovery
-      href: how-to/disaster-recovery.md
-    - name: Security baseline
-      href: /security/benchmark/azure/baselines/azure-ai-studio-security-baseline
+    - name: Role-based access control in Azure AI Studio
+      href: concepts/rbac-ai-studio.md
+  - name: Network security
+    items:
+    - name: Configure managed network
+      href: how-to/configure-managed-network.md
+    - name: Configure private link
+      href: how-to/configure-private-link.md
+    - name: Configure custom DNS
+      href: /azure/machine-learning/how-to-custom-dns?context=/azure/ai-studio/context/context
+    - name: Secure playground chat
+      href: how-to/secure-data-playground.md
+    - name: Troubleshoot secure project connectivity
+      href: how-to/troubleshoot-secure-connection-project.md
+  - name: Data protection & encryption
+    items:
+    - name: Configure customer-managed keys
+      href: concepts/encryption-keys-portal.md
+    - name: Rotate keys
+      href: ../ai-services/rotate-keys.md?context=/azure/ai-studio/context/context
+  - name: Vulnerability management
+    href: concepts/vulnerability-management.md
+  - name: Disaster recovery
+    href: how-to/disaster-recovery.md
+  - name: Security baseline
+    href: /security/benchmark/azure/baselines/azure-ai-studio-security-baseline
 - name: Responsible AI
   items:
   - name: Overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セクションの整理と名称変更による TOC の更新"
}
```

### Explanation
このコードの差分は、AI Studioの目次ファイル（`toc.yml`）において、セクションの名称と構成が変更されたことを示しています。具体的には、「Infrastructure & security」というセクションが「Security & Governance」に改名され、その内容も整理されています。

変更された主な点には、以下のものがあります：
- セクションの名称が変更され、より明確なトピックの明示が行われました。
- 各サブセクションの位置が見直され、関連情報が整理されています。たとえば、役割に基づくアクセス制御やネットワークセキュリティに関するトピックが上下に整列され、より分かりやすくなりました。
- 一部の項目が移動され、セクションが一貫した形で構成されています。これにより、ユーザーが安全性とガバナンスに関する情報を素早く見つけやすくなっています。

この更新は、ユーザーが必要な情報にアクセスしやすくなることを目的としており、全体としてナビゲーションの効率性を向上させています。これは、より良いユーザー体験を提供するための重要なステップとなります。


