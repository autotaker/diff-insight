---
date: '2024-11-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e12bec9...MicrosoftDocs:6042051
summary: この変更では、ストレージ接続に関するドキュメントが更新され、設定手順やトラブルシューティングガイドが改善されました。これにより、ユーザーがネットワーク接続の問題を効果的に解決できるようになっています。主に既存の情報が具体的で理解しやすくなったことが強調され、破壊的な変更はありません。全体として、このアップデートはユーザビリティの向上を目指し、ストレージ接続問題の早期解決を支援することが期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e12bec9...MicrosoftDocs:6042051){target="_blank"}

# Highlights
この変更では、ストレージ接続に関するドキュメントの表現が更新され、具体的な設定手順やトラブルシューティングガイドが改善されています。これにより、ユーザーがプロジェクトで発生する可能性のあるネットワーク接続の問題をより効果的に解決できるようになっています。

## New features
特に新機能というよりは、既存のドキュメント内容がより具体的で理解しやすくなるように改善されました。

## Breaking changes
破壊的変更は特にありません。既存の内容を明確化する更新が中心です。

## Other updates
- 表現の変更により、ユーザーが直面するストレージ接続の問題をより効果的に解決できるよう、手順が詳細化されました。

# Insights
このアップデートは、主にドキュメントの改善を目的としています。ストレージ接続に関して、より明確な情報を提供することで、ユーザーが接続に関する問題を自力で解決しやすくなることが狙いです。特に、ストレージアカウントのネットワークアクセス設定が操作に与える影響がより詳しく説明されており、観点としてはユーザーエクスペリエンスの向上が強調されています。

ドキュメントの変更は、企業がユーザビリティを高めようとする努力の一環であり、これによりユーザーが抱えるストレージ接続問題の早期解決を支援することが期待されます。技術者が問題に直面したとき、記載された手順に従うことで迅速に解決策を見出し、サービスを最大限に活用できるようになります。これにより、プロジェクトの効率も向上し、スムーズな開発進行が可能となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [create-projects.md](#item-cb10b3) | minor update | ストレージ接続に関する注意文の更新 | modified | 1 | 1 | 2 | 
| [troubleshoot-secure-connection-project.md](#item-32d5c4) | minor update | 接続トラブルシューティングガイドの更新 | modified | 6 | 5 | 11 | 


# Modified Contents
## articles/ai-studio/how-to/create-projects.md{#item-cb10b3}

<details>
<summary>Diff</summary>
````diff
@@ -126,7 +126,7 @@ In addition, a number of resources are only accessible by users in your project
    | workspacefilestore | {project-GUID}-code | Hosts files created on your compute and using prompt flow |
 
 > [!NOTE]
-> Storage connections are not created directly with the project when your storage account has public network access set to disabled. These are created instead when a first user accesses AI Studio over a private network connection. [Troubleshoot storage connections](troubleshoot-secure-connection-project.md#troubleshoot-missing-storage-connections)
+> Storage connections are not created directly with the project when your storage account has public network access set to disabled. These are created instead when a first user accesses AI Studio over a private network connection. [Troubleshoot storage connections](troubleshoot-secure-connection-project.md#troubleshoot-configurations-on-connecting-to-storage)
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストレージ接続に関する注意文の更新"
}
```

### Explanation
このコードの変更は、ストレージ接続に関する注意文の修正を含むマイナーなアップデートです。具体的には、元の文から「missing storage connections」という表現が「configurations on connecting to storage」という表現に変更されました。これにより、ストレージ接続の問題をトラブルシューティングする際のガイドラインがより明確になり、ユーザーがアクセスする際のネットワーク接続に関連する設定について、より適切な情報が提供されることを意図しています。この変更は、プロジェクトのストレージアカウントがパブリックネットワークアクセスが無効にされている場合の挙動に関する注意を強調しています。

## articles/ai-studio/how-to/troubleshoot-secure-connection-project.md{#item-32d5c4}

<details>
<summary>Diff</summary>
````diff
@@ -123,13 +123,14 @@ If you use a proxy, it may prevent communication with a secured project. To test
 * Configure your proxy server to forward DNS requests to Azure DNS.
 * Ensure that the proxy allows connections to AML APIs, such as "*.\<region\>.api.azureml.ms" and "*.instances.azureml.ms"
 
-## Troubleshoot missing storage connections
+## Troubleshoot configurations on connecting to storage
 
 When you create a project, a number of connections to Azure storage are auto-created for data upload scenarios and artifact storage including prompt flow. When your hub's associated Azure Storage account is having public network access set to 'Disabled', there may be a delay in these storage connections to be created. 
 
 Try the following steps to troubleshoot:
-
 1. In Azure Portal, check the network settings of the storage account that is associated to your hub.
-1. Review your internet connection, and make sure you are using a private connection that is allowed by your storage account.
-1. Navigate to AI Studio > your project > project settings. 
-1. Refresh the page. A number of connections should be created including 'workspaceblobstore'.
+  * If public network access is set to __Enabled from selected virtual networks and IP addresses__, ensure the correct IP address ranges are added to access your storage account.
+  * If public network access is set to __Disabled__, ensure you have a private endpoint configured from your Azure virtual network to your storage account with Target sub-resource as blob. In addition, you must grant the [Reader](/azure/role-based-access-control/built-in-roles#reader) role for the storage account private endpoint to the managed identity.
+2. In Azure Portal, navigate to your AI Studio hub. Ensure the managed virtual network is provisioned and the outbound private endpoint to blob storage is Active. For more on provisioning the managed virtual network, see [How to configure a managed network for Azure AI Studio hubs](configure-managed-network.md).
+3. Navigate to AI Studio > your project > project settings. 
+4. Refresh the page. A number of connections should be created including 'workspaceblobstore'.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "接続トラブルシューティングガイドの更新"
}
```

### Explanation
このコードの変更は、接続トラブルシューティングガイドの一部を更新したもので、特にストレージ接続に関する手順が改善されています。タイトルが「missing storage connections」から「configurations on connecting to storage」に変更され、より具体的な内容に焦点を当てています。

新たに追加された内容には、パブリックネットワークアクセスの設定に応じたストレージアカウントへのアクセス手順が含まれています。また、具体的な手順がリスト形式で詳しく提示されており、プライベートエンドポイントの設定や、Azureポータルでの確認作業が追加されています。これにより、ユーザーがストレージ接続の問題を解決するための手順がより明確になり、効果的なトラブルシューティングが可能になります。全体として、この変更はユーザーの利便性を向上させることを目的としています。


