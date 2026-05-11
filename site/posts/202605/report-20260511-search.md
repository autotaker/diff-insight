---
date: '2026-05-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2cf0ebe...MicrosoftDocs:23f3054
summary: このコード差分には、Azure OpenAI関連ドキュメントに対する2つのマイナーアップデートが含まれています。新機能として、API管理を通じたロードバランシングに関する推奨や、トークン制限超過時のサポートケース作成方法、ベクトライザのベストプラクティスに関する新規セクションが追加されました。特に大きな破壊的変更はありませんが、両ドキュメントの最終更新日が修正されました。この更新は、Azure
  OpenAIサービスの利用に関する具体的な運用指針を提供し、ユーザーの効率的な利用を促進します。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2cf0ebe...MicrosoftDocs:23f3054){target="_blank"}

# ハイライト
このコード差分では、Azure OpenAI関連ドキュメントの2つにわたるマイナーアップデートが含まれています。具体的な新機能や大きな破壊的変更はありませんが、ユーザーがサービスを利用する際に役立つ重要な推奨事項が追加されています。

## 新機能
- API管理を通じたロードバランシングの導入に関する推奨。
- トークン制限超過時にサポートケースを作成する方法の強調。
- ベクトライザ利用に対するベストプラクティスの新規セクション。

## 破壊的変更
- 特に大きな破壊的変更はありません。

## その他の更新
- 両ドキュメントの最終更新日の訂正。

# インサイト
今回の更新は、Azure OpenAIの利用における具体的で現実的な運用アドバイスを強化するものです。この結果、ドキュメントを参照する開発者やエンジニアは、Azure OpenAIサービスをより効果的に利用し、発生しうる課題を未然に防ぐための手法を学ぶことができます。

特に、API管理を通じたロードバランシングの導入に関する推奨は、サービスのスケーラビリティとパフォーマンスの向上に寄与します。429エラーの回避という観点においても、多くのユーザーにとって有用な情報です。また、トークン制限に関する注意点は、サービス利用における課金システムとの関係をより明確にし、無駄なコストの発生を避ける助けになります。

ベクトライザのベストプラクティスの追加によって、ユーザーは異なる用途に応じたデプロイメントの分離や、地域的な制約を考慮した設計を行う際の指針を得られます。これにより、最適な設計・実装が可能となり、より良いユーザー体験を提供できます。

全体として、これらの更新により、Azure OpenAIサービスの利用者は、サービスの特性と提供されるサポートを最大限に活用できるようになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-azure-openai-embedding.md](#item-3eca57) | minor update | Azure OpenAI Embedding Skill に関する更新 | modified | 3 | 1 | 4 | 
| [vector-search-vectorizer-azure-open-ai.md](#item-e75cee) | minor update | Azure OpenAI ベクトライザに関するベストプラクティスの追加 | modified | 16 | 1 | 17 | 


# Modified Contents
## articles/search/cognitive-search-skill-azure-openai-embedding.md{#item-3eca57}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: reference
-ms.date: 10/23/2025
+ms.date: 05/09/2025
 ---
 
 #	Azure OpenAI Embedding skill
@@ -142,6 +142,8 @@ The following are some best practices you need to consider when utilizing this s
 
 - Your Azure OpenAI instance should be in the same region or at least geographically close to the region where your AI Search service is hosted. This reduces latency and improves the speed of data transfer between the services.
 
+- To avoid experiencing 429 error codes often, consider implementing load balancing via [API Management](/azure/api-management/) by implementing a gateway [/azure/architecture/ai-ml/guide/azure-openai-gateway-multi-backend] in front of multiple Azure OpenAI embedding model deployments.
+
 -	If you have a larger than default Azure OpenAI TPM (Tokens per minute) limit as published in [quotas and limits](/azure/ai-services/openai/quotas-limits) documentation, open a [support case](/azure/azure-portal/supportability/how-to-create-azure-support-request) with the Azure AI Search team, so this can be adjusted accordingly. This helps your indexing process not being unnecessarily slowed down by the documented default TPM limit, if you have higher limits.
 
 - For examples and working code samples using this skill, see the following links:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Embedding Skill に関する更新"
}
```

### Explanation
この変更は、「Azure OpenAI Embedding Skill」に関するドキュメントの小規模な更新を反映しています。具体的には、最終更新日が「2025年10月23日」から「2025年5月9日」に変更され、いくつかの新しい推奨事項が追加されました。特に、API管理を介したロードバランシングの実装についてのアドバイスが含まれており、これにより429エラーコードの発生を避けることができると述べています。また、ユーザーがAzure OpenAIのトークン制限を超える場合のサポートケースの作成についての指示が強調されています。この更新により、ユーザーはAzure OpenAIサービスの利用方法に関する重要な情報をより効果的に活用できるようになります。

## articles/search/vector-search-vectorizer-azure-open-ai.md{#item-e75cee}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-search
 ms.custom:
   - build-2024
 ms.topic: concept-article
-ms.date: 10/23/2025
+ms.date: 05/09/2026
 ms.update-cycle: 365-days
 ---
 
@@ -74,6 +74,21 @@ The expected field dimensions for a field configured with an Azure OpenAI vector
 ]
 ```
 
+## Best practices
+
+The following are some best practices you need to consider when utilizing this vectorizer:
+
+- If you are hitting your Azure OpenAI TPM (Tokens per minute) limit, consider the [quota limits advisory](/azure/ai-services/openai/quotas-limits) so you can address accordingly. Refer to the [Azure OpenAI monitoring](/azure/ai-services/openai/how-to/monitoring) documentation for more information about your Azure OpenAI instance performance.
+
+-	The Azure OpenAI embeddings model deployment you use for this vectorizer should be ideally separate from the deployment used for other use cases, including the [embedding skill](cognitive-search-skill-azure-openai-embedding.md). This helps each deployment to be tailored to its specific use case, leading to optimized performance and identifying traffic from the indexer and the index embedding calls easily.
+
+- Your Azure OpenAI instance should be in the same region or at least geographically close to the region where your AI Search service is hosted. This reduces latency and improves the speed of data transfer between the services.
+
+- To avoid experiencing 429 error codes often, consider implementing load balancing via [API Management](/azure/api-management/) by implementing a gateway [/azure/architecture/ai-ml/guide/azure-openai-gateway-multi-backend] in front of multiple Azure OpenAI embedding model deployments.
+
+-	If you have a larger than default Azure OpenAI TPM (Tokens per minute) limit as published in [quotas and limits](/azure/ai-services/openai/quotas-limits) documentation, open a [support case](/azure/azure-portal/supportability/how-to-create-azure-support-request) with the Azure AI Search team, so this can be adjusted accordingly. This helps your indexing process not being unnecessarily slowed down by the documented default TPM limit, if you have higher limits.
+
+
 ## See also
 
 + [Integrated vectorization](vector-search-integrated-vectorization.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI ベクトライザに関するベストプラクティスの追加"
}
```

### Explanation
この変更は、「Azure OpenAI ベクトライザ」に関するドキュメントに対する小規模な更新を行っています。主な改訂点として、最終更新日が「2025年10月23日」から「2026年5月9日」に変更されました。また、ベストプラクティスに関する新たなセクションが追加され、ユーザーがベクトライザを活用する上で考慮すべき事項が明確に示されています。

新たに追加された内容には、Azure OpenAIのトークン制限についてのアドバイスや、異なる用途に対するデプロイメントの分離、地域に関する考慮点、API管理を通じたロードバランシングの実装についての推奨が含まれています。これにより、ユーザーはパフォーマンスを最適化し、エラーコードを回避するための具体的な手段を把握できるようになります。このアップデートは、Azure OpenAIサービスを利用するユーザーにとって有益なリソースとなります。


