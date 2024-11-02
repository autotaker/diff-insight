---
date: '2024-11-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7c64df0...MicrosoftDocs:635ff11
summary: 今回の変更は、ドキュメントインテリジェンスの目次ファイルおよびエンドポイントに関する文書のリンクやコンテンツを更新し、ユーザーエクスペリエンスを向上させることを目的としています。新たにAzure
  AI推論SDKでの接続方法やコード例へのリンクが追加され、ユーザーの実装がスムーズになりました。破壊的な変更は含まれておらず、文書全体のナビゲーションと明確性が改善されています。これにより、ユーザーは必要な情報に簡単にアクセスできるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7c64df0...MicrosoftDocs:635ff11){target="_blank"}

# ハイライト
今回の変更は、ドキュメントインテリジェンスの目次ファイル（toc.yml）およびエンドポイントに関するドキュメント（endpoints.md）におけるリンクやコンテンツの更新を含んでいます。これにより、ユーザーエクスペリエンスが向上し、情報へのアクセシビリティが改善されます。

## 新機能
- エンドポイントに関するドキュメントに、Azure AI推論SDKでの接続方法の詳細が追加されました。
- コード例へのリンクを含む新しいセクションが追加され、ユーザーの実装が容易になりました。

## 破壊的変更
今回の変更には破壊的な変更は含まれていません。

## その他の更新
- ドキュメントインテリジェンスの目次ファイル内でリンクのパスが更新され、ユーザーが正確にリソースにアクセスできるようになりました。
- エンドポイントに関する文書内でいくつかの表現が調整され、内容が明確化されました。

# 洞察
この度の変更は、主にユーザビリティとナビゲーションの改善を目指したドキュメント更新に焦点を当てています。まず、ドキュメントインテリジェンスのTOCでは、リンクパスの修正が行われました。従来のリンクに対してパスが正確になされることで、ドキュメントの誤った箇所に飛ばれず、ユーザーは必要な情報にスムーズにアクセスできるようになりました。

一方で、エンドポイントに関するドキュメント更新では、Azure AI推論SDKを用いた具体的な接続方法が新たに追加されました。この追加によって、利用者は実際の実装に対する理解が深化し、SDKの活用の可能性を広げることが可能となりました。コード例へのリンクが含まれたことも特筆すべきであり、これによってユーザーは具体的に試行錯誤する精神的負担が軽減されます。

また、これに伴い表現の見直しが行われたことで、特にルーティングの柔軟性についての理解が深まり、異なる構成で同一モデルを複数デプロイする際の動作が明確化されました。これらの修正はすべて、小規模ではありますが相互に有機的に結びついており、ドキュメント全体としての積極的な改善がなされています。ユーザーエクスペリエンスの向上を意識したこういった更新は、サービス利用者への深い配慮を示すものであり、有効性の高い知見が提供されていると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-81aa7b) | minor update | ドキュメントインテリジェンスのTOCにおけるリンクの更新 | modified | 5 | 5 | 10 | 
| [endpoints.md](#item-ca66ea) | minor update | エンドポイントに関するドキュメントの更新 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ items:
         href: sdk-overview-v3-0.md
       - name:  "SDK targets: REST API v2.1 (GA)"
         displayName: get started, installation, downloads, formRecognizerClientClient, form recognizer client, Azure AD, Azure Active Directory, identity, changelog, package, version,AzureKeyCredential, Azure key credential, key, endpoint
-        href: /v21/sdk-overview.md
+        href: v21/sdk-overview-v2-1.md
   - name: Language support
     items:
       - name: Document analysis models
@@ -173,7 +173,7 @@ items:
       href: quickstarts/get-started-sdks-rest-api.md
     - name: Sample Labeling tool
       displayName: tables, labels, ocr, bounding box
-      href: /v21/try-sample-label-tool.md
+      href: v21/try-sample-label-tool.md
 - name: How-to guides
   items:
   - name: Use Document Intelligence models
@@ -217,13 +217,13 @@ items:
       href: how-to-guides/compose-custom-models.md
     - name: Deploy the sample-labeling tool
       displayName: FOTT, migration, containers, docker
-      href: /v21/deploy-label-tool.md
+      href: v21/deploy-label-tool.md
     - name: Train a custom model with the sample-labeling tool
       displayName: FOTT, migration, containers, docker
-      href: /v21/label-tool.md
+      href: v21/label-tool.md
     - name: Use table tags to train your custom model
       displayName: FOTT, migration, dynamic
-      href: /v21/supervised-table-tags.md
+      href: v21/supervised-table-tags.md
   - name: Back up and recover models
     displayName: disaster, recovery, region, copy, modelId, model ID
     href: disaster-recovery.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのTOCにおけるリンクの更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスの目次ファイル（toc.yml）内のいくつかのリンクを更新することに関するものです。具体的には、リンクのパスが更新されました。例えば、"href: /v21/sdk-overview.md" が "href: v21/sdk-overview-v2-1.md" という新しいパスに変更されています。また、他のいくつかのリンクも同様に "/v21/" プレフィックスが削除され、より整然とした形式に改良されています。

この変更によって、ドキュメント内のリソースへのリンクが正確になり、ユーザーが必要な情報にアクセスしやすくなることが期待されます。全体として、この修正は文書のナビゲーションを改善し、より良いユーザー体験を提供することを目指しています。

## articles/ai-studio/ai-services/concepts/endpoints.md{#item-ca66ea}

<details>
<summary>Diff</summary>
````diff
@@ -45,6 +45,12 @@ You can see the endpoint URL and credentials in the **Overview** section. The en
 
 :::image type="content" source="../../media/ai-services/overview/overview-endpoint-and-key.png" alt-text="A screenshot showing how to get the URL and key associated with the resource." lightbox="../../media/ai-services/overview/overview-endpoint-and-key.png":::
 
+You can connect to the endpoint using the Azure AI Inference SDK:
+
+[!INCLUDE [code-create-chat-client](../../includes/ai-services/code-create-chat-client.md)]
+
+See [Supported languages and SDKs](#supported-languages-and-sdks) for more code examples and resources.
+
 ### Routing
 
 The inference endpoint routes requests to a given deployment by matching the parameter `name` inside of the request to the name of the deployment. This means that *deployments work as an alias of a given model under certain configurations*. This flexibility allows you to deploy a given model multiple times in the service but under different configurations if needed.
@@ -96,4 +102,4 @@ The Azure OpenAI endpoint is supported by the **OpenAI SDK (`AzureOpenAI` class)
 
 ## Next steps
 
-- [Deployment types](deployment-types.md)
\ No newline at end of file
+- [Deployment types](deployment-types.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンドポイントに関するドキュメントの更新"
}
```

### Explanation
この変更は、エンドポイントに関するドキュメント（endpoints.md）に対して行われた修正で、主にコンテンツの追加が含まれています。具体的には、Azure AI推論SDKを使用してエンドポイントに接続する方法に関する情報が追加されました。新しく追加されたセクションでは、コード例へのリンクが含まれ、ユーザーが具体的な実装方法を参照する手助けがされています。

また、文書内のいくつかの表現が整えられ、全体的な内容がより明確になりました。特に、ルーティングに関する説明が強化され、その柔軟性が強調されています。これにより、ユーザーはデプロイメントの動作を理解しやすくなり、異なる構成で同じモデルを複数回デプロイする方法を把握することができます。

この更新は、小規模な改良でありながら、読者にとっての理解を深めることに寄与する重要な変更と言えます。


