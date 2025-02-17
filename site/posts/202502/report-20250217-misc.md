---
date: '2025-02-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1cff62f...MicrosoftDocs:caf7737
summary: '`connections-add-sdk.md`ファイルが更新され、セキュリティ関連の情報が調整されました。Microsoft Entra IDやAPIキーに関する注意事項が強調され、Azure
  Key Vaultの使用が推奨されています。また、目次から「Get started」が削除され、構造が簡潔になりました。特に破壊的な変更はありませんが、目次の変更がナビゲーションに影響する可能性があります。この改訂により、開発者はSDKをより安全に使用できるようになり、ユーザーエクスペリエンスが向上します。'
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1cff62f...MicrosoftDocs:caf7737){target="_blank"}

# Highlights
`connections-add-sdk.md`ファイルの内容が更新され、セキュリティ関連の情報が調整されました。特に、Microsoft Entra IDやAPIキーに関する注意事項が強調され、Azure Key Vaultの使用が推奨されるようになりました。また、`toc.yml`ファイルの目次から「Get started」という項目が削除され、構造が簡潔になっています。

## New features
- 新しいインクルード文が追加され、APIキーの安全な管理に関して、Azure Key Vaultの使用が強調されるようになりました。

## Breaking changes
- 特に破壊的な変更は含まれていませんが、目次から「Get started」の項目が削除されたことで、情報のナビゲーションに影響を及ぼす可能性があります。

## Other updates
- セキュリティに関連する旧推奨事項が削除され、新しいベストプラクティスに置き換えられました。
- 目次の構造が整理され、情報へのアクセスが改善されました。

# Insights
今回の変更は、開発者がより安全にSDKを用いて接続を追加できるようにすることに重点が置かれています。特に、Microsoft Entra IDやAPIキーの取り扱いに関するセキュリティ対策が強調されており、Azure Key Vaultの使用推奨が新たに明示されています。これにより、利用者が認証情報を誤用するリスクが低減され、安全なアプリケーション開発が促進されます。

また、`toc.yml`から「Get started」という項目を削除することにより、ドキュメントの目次が簡潔になり、ユーザーが必要な情報にアクセスしやすくなることが意図されています。これらの変更は、全体としてドキュメントの整合性を高め、ユーザーエクスペリエンスの向上を図るものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [connections-add-sdk.md](#item-14b519) | minor update | SDKを使用した接続の追加に関する文書の更新 | modified | 1 | 5 | 6 | 
| [toc.yml](#item-2745cd) | minor update | AIスタジオの目次から「開始する」に関する項目を削除 | modified | 0 | 1 | 1 | 


# Modified Contents
## articles/ai-studio/how-to/develop/connections-add-sdk.md{#item-14b519}

<details>
<summary>Diff</summary>
````diff
@@ -36,11 +36,7 @@ Connections are a way to authenticate and consume both Microsoft and other resou
 
 There are various authentication methods for the different connection types. When you use Microsoft Entra ID, in addition to creating the connection you might also need to grant Azure role-based access control permissions before the connection can be used. For more information, visit [Role-based access control](../../concepts/rbac-ai-studio.md#scenario-connections-using-microsoft-entra-id-authentication).
 
-> [!IMPORTANT]
-> We recommend Microsoft Entra ID authentication with [managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview) to avoid storing credentials with your applications that run in the cloud.
->
-> If you use an API key, store it securely somewhere else, such as in [Azure Key Vault](/azure/key-vault/general/overview). Don't include the API key directly in your code, and never post it publicly.
-
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 ## Azure OpenAI Service
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDKを使用した接続の追加に関する文書の更新"
}
```

### Explanation
この変更では、`connections-add-sdk.md`ファイルの内容が更新され、主にセキュリティに関連する情報が調整されました。具体的には、Microsoft Entra IDとAPIキーの使用に関する重要な注意事項が強調され、APIキーを安全に保管する方法としてAzure Key Vaultの使用を推奨する内容が明確にされました。このアップデートは、開発者が認証情報の管理とセキュリティを確保するための重要なベストプラクティスを強調しています。変更点として、重要な注意事項を示すための新しいインクルード文が追加された一方で、古い推奨事項については削除されました。これにより、Documentationは最新の推奨事項に基づき、より安全な開発を促進します。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,6 @@ items:
   href: what-is-ai-studio.md
 - name: What's new in Azure AI Foundry?
   href: whats-new-ai-foundry.md
-- name: Get started
 - name: Overview
   expanded: true
   items:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオの目次から「開始する」に関する項目を削除"
}
```

### Explanation
この変更では、`toc.yml`ファイル内の目次が更新されました。具体的には、「Get started」という項目が削除され、その結果、他の項目との整合性が保たれています。この削除は、目次をより簡潔にし、読者が必要な情報に迅速にアクセスできるようにすることを目的としています。変更は1行で、他の関連するコンテンツへのリンクを維持しながら、構造を最適化しています。これにより、ユーザーがAIスタジオの情報を見つけやすくなることが期待されます。


